from amr_metadata import get_metadata


gene = "blaTEM"

metadata = get_metadata(gene)

print("Gene:", gene)
print("Mechanism:", metadata["mechanism"])
print("Antibiotic class:", metadata["antibiotic_class"])
print("Description:", metadata["description"])