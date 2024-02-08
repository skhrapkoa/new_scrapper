INSTRUCTION = f'''You are a helpful assistant.'''

TEXT = (
    f'''We are an IT company offering computer vision services for manufacturing like:\n\n'''
    
    f'''1. Quality Control: Automated inspection of products, detecting defects and ensuring high-quality manufacturing.\n'''
    f'''2. Predictive Maintenance for Machinery: Equipment monitoring and machinery health, predicting maintenance needs and minimizing downtime.\n'''
    f'''3. Production Line Monitoring: Counting units, classifications for the efficiency of production lines.\n'''
    f'''4. Automated Defect Detection in Fabrication: Flag defects in fabricated components or materials.\n'''
    f'''5. Automated Assembly Verification: Verify the correct assembly of components on the production line.\n'''
    f'''6. Real-time Inventory Tracking: Monitor and manage inventory levels in real-time.\n'''
    f'''7. Tool Tracking and Optimization: Track the usage and condition of manufacturing tools, optimizing tool changes and maintenance.\n'''
    f'''8. Logistics within the Manufacturing Facility: Monitor vehicles and logistics robots to enhance material handling within the facility.\n'''
    f'''9. Energy Consumption Monitoring: Monitor energy usage on the manufacturing floor and identify opportunities for optimization.\n'''
    f'''10. Worker Safety Monitoring: Ensure compliance with safety protocols on the manufacturing floor.\n'''
    f'''11. Inventory Reordering Automation: Automate the reordering of raw materials and components based on inventory levels.\n\n'''
    
    f'''We need to find the best match for our 1-11 services to the potential customers.\n'''
    f'''For achieving this we select one by one potential customers and collect its public news and posts.\n'''
    f'''I will put these news and posts after the tag "Newsprompt:"\n'''
    f'''Please read through the content and try to understand, which strategic goals are set for this company for the year ahead, and which of them can match our 1-11 services list.\n\n'''
    
    f'''I need an answer in the following structure:\n'''
    f'''Number of service, % of probability of match, Quote from the news that hints at these similarities.\n'''
    f'''Each list item should contain Quote and Rationale short sections with 1-2 lines of arguments.\n'''
    f'''Range this list from high probability to low.\n'''
    f'''Do not add any before and after description, just the list.\n'''
    f'''I need only the top 3 from that list.\n'''
    f'''You can also add two ideas for computer vision for that exact company, which are out of the list of our services.\n\n'''
    
    f'''Newsprompt:\n'''
)
