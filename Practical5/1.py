import matplotlib.pyplot as plt

# 1. Create gene expression dictionary and add MYC gene
gene_expression = {'TP53': 12.4, 'EGFR': 15.1, 'BRCA1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}
print(gene_expression)

# Add MYC gene 
gene_expression['MYC'] = 11.6
print(gene_expression)

# 2. Plot gene expression bar chart (ALL ENGLISH LABELS)
plt.rcParams['font.sans-serif'] = ['Arial']  # Ensure English display

# Extract data for plotting
genes = list(gene_expression.keys())
expression_levels = list(gene_expression.values())

# Draw bar chart
plt.bar(genes, expression_levels ,color = "skyblue")
    
# Add English labels (meet assignment requirements)
plt.title('Gene Expression Levels in Biological Sample', fontsize=14, pad=15)
plt.xlabel('Gene Name', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y-axis grid for readability
plt.show()

# 3. Gene query with error handling
target_gene = 'EGFR' 
if target_gene in gene_expression:
    print(f"Expression level of {target_gene}: {gene_expression[target_gene]}")
else:
    print(f"Error: Gene {target_gene} does not exist in the dataset!")

# 4. Calculate average expression level
total_expression = sum(gene_expression.values())
gene_count = len(gene_expression)
average_expression = total_expression / gene_count

print(f"Total genes: {gene_count} | Average expression level: {average_expression:.2f}")