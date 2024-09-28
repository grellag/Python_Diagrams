from diagrams import Diagram
from diagrams.aws.management import SystemsManager
from diagrams.onprem.database import SQL
from diagrams.custom import Custom

# Create the diagram context
with Diagram("Cache Rebuild Workflow", show=False):
    # Define the job as a process box
    job = Custom("[MSCITA][Rebuild Cache] - PBI - Export - Schedule Leg", "./job_icon.png")
    
    # Define the stored procedure
    sp = SQL("SP_PBI_DCC_Export_Schedule_Leg_H_Cache")

    # Define the stage table and final table
    stage_table = SQL("PBI_DCC_Schedule_Leg_H_temp")
    final_table = SQL("PBI_DCC_Schedule_Leg_H")

    # Define the flow
    job >> sp >> stage_table >> final_table

