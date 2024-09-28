from diagrams import Diagram
from diagrams.aws.management import SystemsManager
from diagrams.onprem.database import MSSQL
from diagrams.custom import Custom
from IPython.display import Image
from PIL import Image as PILImage, ImageDraw, ImageFont
import os

# Define the diagram file name
diagram_file = "Cache_Rebuild_Workflow.png"

# Create the diagram context without the title
with Diagram(
    "Titolo di prova",  # Empty title
    show=False, 
    direction="TB", 
    outformat="png", 
    graph_attr={
        "pad": "0.0",  # No padding around the graph
        "nodesep": "0.1",  # Minimal space between nodes
        "ranksep": "0.1",  # Minimal space between ranks (levels)
        "margin": "0.0",  # No extra margin around the diagram
    },
    node_attr={
        "width": "0.3",  
        "height": "0.3",  
        "fontsize": "5",  
        "fontname": "Arial",  
    },
    edge_attr={
        "penwidth": "1",         # Controls thickness of the arrow line
        "arrowsize": "0.6",      # Controls arrowhead size
        "color": "red",         # Changes arrow color
        "arrowhead": "vee",      # Defines arrowhead style
        "style": "dashed",        # Can be solid, dashed, dotted
    }
):
    job_main = Custom("PBI - Export Stat", "./job_icon.png")
    sp = MSSQL("SP_PBI_DCC_Export_H_Cache")
    stage_table = MSSQL("PBI_DCC_H_temp")
    final_table = MSSQL("PBI_DCC__H")

    # Define dependent jobs
    job_intermodal = Custom("Intermodal", "./job_icon.png")
    job_mtfc = Custom("MTFC", "./job_icon.png")
    job_charge_all = Custom("PBI Charge - ALL", "./job_icon.png")
    job_freight_debtor = Custom("PBI Freight Debtor", "./job_icon.png")
    job_si_monitoring = Custom("PBI SI Monitoring", "./job_icon.png")
    job_bls_vs_emcs = Custom("BLs vs EMCs", "./job_icon.png")
    job_export_seals = Custom("Export Seals", "./job_icon.png")
    job_export_vgm = Custom("Export VGM", "./job_icon.png")
    job_vgm_info = Custom("VGM Info", "./job_icon.png")

    tbl_intermodal = MSSQL("PBI_DCC_Intermodal_cache")
    tbl_mtfc = MSSQL("PBI_DCC_Export_H_cache_MTFC")
    tbl_charge_all = MSSQL("PBI_Charge_Lenavi_MEDLOG")
    tbl_freight_debtor = MSSQL("PBI_BL_List_by_Freight_Debtor")
    tbl_si_monitoring_1 = MSSQL("PBI_SIMonitoring_SI_Detail")
    tbl_si_monitoring_2 = MSSQL("PBI_IFTMIN_eImage_vw")
    tbl_si_monitoring_3 = MSSQL("PBI_DCC_Export_SI_cache")
    tbl_bls_vs_emcs = MSSQL("STATS_DW_Bill_Of_Lading")
    tbl_export_seals = MSSQL("PBI_DCC_Export_H_Cache_Seals")
    tbl_export_vgm = MSSQL("PBI_DCC_Export_H_Cache_VGM")
    tbl_vgm_info = MSSQL("VGMInfo_H")

    # Define the flow
    job_main >> sp >> stage_table >> final_table

    job_intermodal >> tbl_intermodal >> stage_table
    job_mtfc >> tbl_mtfc >> stage_table
    job_charge_all >> tbl_charge_all >> stage_table
    job_freight_debtor >> tbl_freight_debtor >> stage_table
    job_si_monitoring >> tbl_si_monitoring_1 >> stage_table
    job_si_monitoring >> tbl_si_monitoring_2 >> stage_table
    job_si_monitoring >> tbl_si_monitoring_3 >> stage_table
    job_bls_vs_emcs >> tbl_bls_vs_emcs >> stage_table
    job_export_seals >> tbl_export_seals >> stage_table
    job_export_vgm >> tbl_export_vgm >> stage_table
    job_vgm_info >> tbl_vgm_info >> stage_table

# Check if the file was created successfully
if os.path.exists(diagram_file):
    print(f"Diagram saved as: {diagram_file}")
else:
    print("Error: Diagram file not found.")

# Now, add the custom title using PIL
img = PILImage.open(diagram_file)

# Create a drawing context
draw = ImageDraw.Draw(img)

# Load a font (optional: specify the path to a .ttf font if necessary)
try:
    font = ImageFont.truetype("arial.ttf", 8)  # You can adjust font size here
except IOError:
    font = ImageFont.load_default()

# Define text properties
title = "Cache Rebuild Workflow titolo Giorgio"
text_color = (0, 0, 0)  # Black color
text_position = (50, 10)  # Adjust this for proper placement

# Add the title to the image
draw.text(text_position, title, font=font, fill=text_color)

# Save the image with the title
img_with_title = "Cache_Rebuild_Workflow_with_title.png"
img.save(img_with_title)

# Display the saved image in the Jupyter notebook
Image(img_with_title)
