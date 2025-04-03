import pandas as pd
from pgmpy.estimators import HillClimbSearch, BicScore
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
import networkx as nx
import matplotlib.pyplot as plt
import glob
from openpyxl.styles import Font, Alignment, Border, Side

def format_worksheet(worksheet):
    # Define styles
    header_font = Font(bold=True)
    border = Border(left=Side(style='thin'), right=Side(style='thin'),
                   top=Side(style='thin'), bottom=Side(style='thin'))
    
    # Apply formatting to all cells in use
    for row in worksheet.rows:
        for cell in row:
            cell.border = border
            cell.alignment = Alignment(horizontal='center')
            if cell.row == 1:
                cell.font = header_font
    
    # Adjust column widths
    for column in worksheet.columns:
        max_length = 0
        for cell in column:
            try:
                max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        worksheet.column_dimensions[column[0].column_letter].width = max_length + 2
# Load and preprocess the data
df = pd.read_excel("categorized_data.xlsx")
for column in df.columns:
    df[column] = df[column].astype('category')

# Learn the structure of the Bayesian Network
hc = HillClimbSearch(df)
best_model = hc.estimate(scoring_method=BicScore(df))  # Use BIC scoring method
print("Learned Edges:", best_model.edges())

# Create the Bayesian Network
model = BayesianNetwork(best_model.edges())

# Fit the model to learn conditional probabilities
model.fit(df, estimator=MaximumLikelihoodEstimator)


# Print the conditional probability tables (CPTs) for each node
for node in model.nodes():
    cpd = model.get_cpds(node)
    cpd.to_csv(f'new_cpd_{node}.csv')

# Create consolidated Excel file
with pd.ExcelWriter('bayesian_network_cpds.xlsx', engine='openpyxl') as writer:
    for csv_file in glob.glob('cpd_*.csv'):
        sheet_name = csv_file.replace('cpd_', '').replace('.csv', '')
        df = pd.read_csv(csv_file)
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Apply formatting
        worksheet = writer.sheets[sheet_name]
        format_worksheet(worksheet)

graph = nx.DiGraph()
graph.add_edges_from(model.edges())
nx.draw(graph, with_labels=True, node_size=2000, font_size=10, arrowsize=20)
plt.show()