from urllib.request import urlopen

references = {
    "blaSHV": "AF148850.1",
    "blaCTX-M": "DQ343292.1",
    "blaKPC": "AY034847.1",
    "blaNDM": "KP772144.1",
    "blaVIM": "GQ288399.1",
    "blaIMP": "AY055216.1",
    "blaOXA-48": "NG_049762.1",
}

output_file = "beta_lactamase_database.fasta"

with open(output_file, "w", encoding="utf-8") as output:

    # Existing blaTEM reference
    with open(
        "test_sequences/blaTEM.fasta",
        "r",
        encoding="utf-8"
    ) as tem_file:

        lines = tem_file.read().strip().splitlines()
        dna = "".join(lines[1:]).upper()

        output.write(">blaTEM|NCBI:KT867019.1\n")

        for i in range(0, len(dna), 80):
            output.write(dna[i:i + 80] + "\n")

    # Download remaining references
    for gene, accession in references.items():

        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
            f"efetch.fcgi?db=nuccore&id={accession}"
            "&rettype=fasta&retmode=text"
        )

        print(f"Downloading {gene} ({accession})...")

        with urlopen(url) as response:
            sequence = response.read().decode("utf-8")

        lines = sequence.strip().splitlines()
        dna = "".join(lines[1:]).upper()

        output.write(
            f">{gene}|NCBI:{accession}\n"
        )

        for i in range(0, len(dna), 80):
            output.write(dna[i:i + 80] + "\n")

print()
print("Beta-lactamase reference database created.")
