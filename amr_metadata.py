AMR_METADATA = {

    "blaTEM": {
        "family": "TEM",
        "mechanism": "Beta-lactamase production",
        "antibiotic_class": "Beta-lactams",
        "description": (
            "TEM-family beta-lactamase determinant "
            "associated with resistance to beta-lactam "
            "antibiotics."
        )
    },

    "blaSHV": {
        "family": "SHV",
        "mechanism": "Beta-lactamase production",
        "antibiotic_class": "Beta-lactams",
        "description": (
            "SHV-family beta-lactamase determinant "
            "associated with resistance to beta-lactam "
            "antibiotics."
        )
    },

    "blaCTX-M": {
        "family": "CTX-M",
        "mechanism": (
            "Extended-spectrum beta-lactamase production"
        ),
        "antibiotic_class": "Beta-lactams",
        "description": (
            "CTX-M-family extended-spectrum beta-lactamase "
            "determinant associated with resistance to "
            "multiple beta-lactam antibiotics."
        )
    },

    "blaKPC": {
        "family": "KPC",
        "mechanism": "Carbapenemase production",
        "antibiotic_class": "Beta-lactams",
        "description": (
            "KPC-family carbapenemase determinant "
            "associated with resistance to carbapenem "
            "and other beta-lactam antibiotics."
        )
    },

    "blaNDM": {
        "family": "NDM",
        "mechanism": "Metallo-beta-lactamase production",
        "antibiotic_class": "Beta-lactams",
        "description": (
            "NDM-family metallo-beta-lactamase determinant "
            "associated with carbapenem resistance."
        )
    },

    "blaVIM": {
        "family": "VIM",
        "mechanism": "Metallo-beta-lactamase production",
        "antibiotic_class": "Beta-lactams",
        "description": (
            "VIM-family metallo-beta-lactamase determinant "
            "associated with carbapenem resistance."
        )
    },

    "blaIMP": {
        "family": "IMP",
        "mechanism": "Metallo-beta-lactamase production",
        "antibiotic_class": "Beta-lactams",
        "description": (
            "IMP-family metallo-beta-lactamase determinant "
            "associated with carbapenem resistance."
        )
    },

    "blaOXA-48": {
        "family": "OXA-48",
        "mechanism": "Carbapenemase production",
        "antibiotic_class": "Beta-lactams",
        "description": (
            "OXA-48-family class D beta-lactamase "
            "determinant associated with carbapenem "
            "resistance."
        )
    }
}


def get_metadata(gene):

    return AMR_METADATA.get(
        gene,
        {
            "family": "Unknown",
            "mechanism": "Unknown",
            "antibiotic_class": "Unknown",
            "description": "No metadata available."
        }
    )