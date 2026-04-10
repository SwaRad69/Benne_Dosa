import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from e_commerce_data_analytics_automation.tools.custom_tool import DataAnalysisTool





@CrewBase
class ECommerceDataAnalyticsAutomationCrew:
    """ECommerceDataAnalyticsAutomation crew"""

    
    @agent
    def e_commerce_data_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["e_commerce_data_analyst"],
            
            
            tools=[DataAnalysisTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=5,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                
                
            ),
            
        )
    
    @agent
    def business_intelligence_reporter(self) -> Agent:
        
        return Agent(
            config=self.agents_config["business_intelligence_reporter"],
            
            
            tools=[DataAnalysisTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=5,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                
                
            ),
            
        )
    
    @agent
    def duplicate_and_missing_data_detector(self) -> Agent:
        
        return Agent(
            config=self.agents_config["duplicate_and_missing_data_detector"],
            
            
            tools=[DataAnalysisTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=5,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                
                
            ),
            
        )
    
    @agent
    def outlier_and_format_validator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["outlier_and_format_validator"],
            
            
            tools=[DataAnalysisTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=5,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                
                
            ),
            
        )
    
    @agent
    def business_rule_validator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["business_rule_validator"],
            
            
            tools=[DataAnalysisTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=5,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                
                
            ),
            
        )
    

    
    @task
    def duplicate_and_missing_data_detection(self) -> Task:
        return Task(
            config=self.tasks_config["duplicate_and_missing_data_detection"],
            markdown=False,
            
            
        )
    
    @task
    def outlier_and_format_validation(self) -> Task:
        return Task(
            config=self.tasks_config["outlier_and_format_validation"],
            markdown=False,
            
            
        )
    
    @task
    def business_rule_validation(self) -> Task:
        return Task(
            config=self.tasks_config["business_rule_validation"],
            markdown=False,
            
            
        )
    
    @task
    def revenue_analysis_by_category(self) -> Task:
        return Task(
            config=self.tasks_config["revenue_analysis_by_category"],
            markdown=False,
            
            
        )
    
    @task
    def delivery_time_analysis_by_region(self) -> Task:
        return Task(
            config=self.tasks_config["delivery_time_analysis_by_region"],
            markdown=False,
            
            
        )
    
    @task
    def return_rate_analysis_by_payment_method(self) -> Task:
        return Task(
            config=self.tasks_config["return_rate_analysis_by_payment_method"],
            markdown=False,
            
            
        )
    
    @task
    def business_health_summary_report(self) -> Task:
        return Task(
            config=self.tasks_config["business_health_summary_report"],
            markdown=False,
            output_file='output/final_report.txt',
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ECommerceDataAnalyticsAutomation crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="gemini/gemini-2.5-flash"),
        )


