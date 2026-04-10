from crewai.tools import BaseTool
from typing import Type, Optional
import pandas as pd
import os
from pydantic import BaseModel, Field


class DataAnalysisInput(BaseModel):
    """Input schema for Data Analysis Tool."""
    file_path: str = Field(..., description="Full path to the CSV file")
    analysis_type: str = Field(..., description="Type of analysis: duplicates, outliers, discounts, revenue, delivery_time, return_rate")


class DataAnalysisTool(BaseTool):
    name: str = "data_analyzer"
    description: str = (
        "Analyzes e-commerce CSV data and returns calculated results. "
        "Supports: duplicates (count duplicate order_ids), outliers (quantity > 1000), "
        "discounts (invalid 0-100%), revenue (by category), delivery_time (avg by region), "
        "return_rate (by payment method)"
    )
    args_schema: Type[BaseModel] = DataAnalysisInput

    def _run(self, file_path: str, analysis_type: str) -> str:
        """Perform data analysis on CSV"""
        try:
            # Clean path
            resolved_path = file_path.strip('"').strip("'")
            
            if not os.path.exists(resolved_path):
                return f"Error: File not found at {resolved_path}"
            
            # Load full dataset
            df = pd.read_csv(resolved_path)
            
            # Duplicates analysis
            if analysis_type == "duplicates":
                dup_count = df['order_id'].duplicated().sum()
                null_count = df.isnull().sum().sum()
                return f"duplicate_order_ids={dup_count}, total_null_cells={null_count}"
            
            # Outliers analysis
            elif analysis_type == "outliers":
                qty_outliers = (df['quantity'] > 1000).sum()
                price_errors = df['unit_price'].isnull().sum()
                return f"quantity_outliers={qty_outliers}, price_format_errors={price_errors}"
            
            # Discount validation
            elif analysis_type == "discounts":
                invalid = ((df['discount_percent'] < 0) | (df['discount_percent'] > 100)).sum()
                return f"invalid_discounts={invalid}"
            
            # Revenue by category
            elif analysis_type == "revenue":
                df_clean = df.dropna(subset=['quantity', 'unit_price', 'discount_percent'])
                df_clean['revenue'] = df_clean['quantity'] * df_clean['unit_price'] * (1 - df_clean['discount_percent']/100)
                revenue_by_cat = df_clean.groupby('product_category')['revenue'].sum().sort_values(ascending=False)
                result = "\n".join([f"{cat}: ${rev:.2f}" for cat, rev in revenue_by_cat.items()])
                return result
            
            # Delivery time by region
            elif analysis_type == "delivery_time":
                df_clean = df.dropna(subset=['delivery_days'])
                avg_by_region = df_clean.groupby('customer_region')['delivery_days'].mean().sort_values(ascending=False)
                result = "\n".join([f"{region}: {avg:.2f} days average" for region, avg in avg_by_region.items()])
                return result
            
            # Return rate by payment method
            elif analysis_type == "return_rate":
                df_clean = df.dropna(subset=['payment_method'])
                df_clean['is_returned'] = (df_clean['return_status'] == 'Returned').astype(int)
                return_by_method = df_clean.groupby('payment_method').apply(
                    lambda x: (x['is_returned'].sum() / len(x) * 100) if len(x) > 0 else 0
                ).sort_values(ascending=False)
                result = "\n".join([f"{method}: {rate:.2f}%" for method, rate in return_by_method.items()])
                return result
            
            else:
                return f"Unknown analysis type: {analysis_type}"
                
        except Exception as e:
            return f"Error: {str(e)}"
