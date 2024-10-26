# Modules, Packages, and Libraries: 

Understanding the Key Differences in Python.

[Articolo originale: Modules, Packages, and Libraries: Understanding the Key Differences in Python](https://medium.com/pythoneers/modules-packages-and-libraries-understanding-the-key-differences-in-python-d8f130a0e29d)


```mermaid
---
config:
  look: handDrawn
  theme: forest
  layout: dagre
---
graph LR;
    A[Python Concepts]

    %% Subgraphs with bold titles using HTML tags
    subgraph MODULI
        B1[Python File]
        B2[Contains Functions, Classes, Variables]
        B3[Improves Readability & Maintainability]
    end
    subgraph PACKAGES
        C1[Folder]
        C2[Contains Modules]
        C3[Includes __init__.py]
        C4[Groups Related Modules]
    end
    subgraph LIBRARIES   
        D1[Collection of Modules and Packages]
        D2[Installed via pip]
        D3[Example: matplotlib]
        D3 --> E1[Contains Several Packages]
        D3 --> E2[Contains Several Modules]
        E1 --> F[Importing: import matplotlib.pyplot as plt]
        E1 --> G[Used for Data Visualization]
    end

    %% Direct connections from A to each node
    A --> B1
    A --> B2
    A --> B3
    A --> C1
    A --> C2
    A --> C3
    A --> C4
    A --> D1
    A --> D2
    A --> D3

    %% Apply yellow background color to each node in subgraphs
    style B1 fill:#FFFF99,stroke:#333,stroke-width:1px
    style B2 fill:#FFFF99,stroke:#333,stroke-width:1px
    style B3 fill:#FFFF99,stroke:#333,stroke-width:1px
    style C1 fill:#FFFF99,stroke:#333,stroke-width:1px
    style C2 fill:#FFFF99,stroke:#333,stroke-width:1px
    style C3 fill:#FFFF99,stroke:#333,stroke-width:1px
    style C4 fill:#FFFF99,stroke:#333,stroke-width:1px
    style D1 fill:#FFFF99,stroke:#333,stroke-width:1px
    style D2 fill:#FFFF99,stroke:#333,stroke-width:1px
    style D3 fill:#FFFF99,stroke:#333,stroke-width:1px
    style E1 fill:#FFFF99,stroke:#333,stroke-width:1px
    style E2 fill:#FFFF99,stroke:#333,stroke-width:1px
    style F fill:#FFFF99,stroke:#333,stroke-width:1px
    style G fill:#FFFF99,stroke:#333,stroke-width:1px
