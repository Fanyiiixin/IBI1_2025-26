# import the matplotlib
import matplotlib.pyplot as plt

# --------------------------
# 1. create initial gene_expression dictionary
# --------------------------
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}


print(gene_expression)

# --------------------------
# 2. add the new gene MYC to the dictionary
# --------------------------
gene_expression["MYC"] = 11.6
print(gene_expression)

# --------------------------
# 3. draw the bar chart
# --------------------------
# extract gene name and expression value
genes = list(gene_expression.keys())
expressions = list(gene_expression.values())

# create the canvas
plt.figure(figsize=(8, 5))

# draw
plt.bar(genes, expressions)

# add labels and title
plt.xlabel("Gene Name", fontsize=12)
plt.ylabel("Expression Level", fontsize=12)
plt.title("Gene Expression Levels in Biological Sample", fontsize=14, pad=15)


# show the figure
plt.show()

# --------------------------
# 4. look up for the gene 
# --------------------------
# define interest gene
gene_of_interest = "MYC"

# check whether the gene exists in the dictionary and return the result
if gene_of_interest in gene_expression:
    print(gene_of_interest,"'s expression value is " )
    print(gene_expression[gene_of_interest])
else:
    print(gene_of_interest,"is not in the dataset")

# --------------------------
# 5. calculate average expression level
# --------------------------
average_expression = sum(expressions) / len(expressions)
print("Average gene expression level: ",average_expression)