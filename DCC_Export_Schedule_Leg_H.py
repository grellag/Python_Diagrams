from diagrams import Diagram
from diagrams.aws.management import SystemsManager
from diagrams.onprem.database import MSSQL
from diagrams.custom import Custom
from IPython.display import Image
import os


# Define the diagram file name
diagram_file = "Cache_Rebuild_Workflow.png"

# Create the diagram context
with Diagram("Cache Rebuild Workflow", show=False, direction="TB", outformat="png"):
    # Define the job as a process box
    job = Custom("[MSCITA][Rebuild Cache] - PBI - Export - Schedule Leg", "./job_icon.png")
    
    # Define the stored procedure
    sp = MSSQL("SP_PBI_DCC_Export_Schedule_Leg_H_Cache")

    # Define the stage table and final table
    stage_table = MSSQL("PBI_DCC_Schedule_Leg_H_temp")
    final_table = MSSQL("PBI_DCC_Schedule_Leg_H")

    # Define the flow
    job >> sp >> stage_table >> final_table

# Check if the file was created successfully
if os.path.exists(diagram_file):
    print(f"Diagram saved as: {diagram_file}")
else:
    print("Error: Diagram file not found.")

# Display the saved image in the Jupyter notebook
Image(diagram_file)

