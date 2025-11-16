from django.shortcuts import render

def index(request):
    data = [
        {
            "original": "తాజ్ మహల్ - భారతదేశం",
            "translated": "Taj Mahal — India",
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/da/Taj-Mahal.jpg"
        },
        {
            "original": "చైనా మహా ప్రాచీర్",
            "translated": "Great Wall of China — China",
            "image": "https://upload.wikimedia.org/wikipedia/commons/1/10/20090529_Great_Wall_8185.jpg"
        },
        {
            "original": "పెట్రా - జోర్డాన్",
            "translated": "Petra — Jordan",
            "image": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Al_Khazneh.jpg"
        },
        {
            "original": "క్రైస్ట్ ది రిడీమర్ - బ్రెజిల్",
            "translated": "Christ the Redeemer — Brazil",
            "image": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Cristo_Redentor_-_Rio_de_Janeiro%2C_Brasil.jpg"
        },
        {
            "original": "మాచూ పిచ్చూ - పెరూ",
            "translated": "Machu Picchu — Peru",
            "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Machu_Picchu%2C_Peru.jpg"
        },
        {
            "original": "చిచెన్ ఇట్జా - మెక్సికో",
            "translated": "Chichen Itza — Mexico",
            "image": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Chichen_Itza_3.jpg"
        },
        {
            "original": "కొలొసియమ్ - ఇటలీ",
            "translated": "Colosseum — Italy",
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/de/Colosseo_2020.jpg"
        },
        {
            "original": "ఐఫిల్ టవర్ - ఫ్రాన్స్",
            "translated": "Eiffel Tower — France",
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg"
        },
        {
            "original": "మౌంట్ ఫుజీ - జపాన్",
            "translated": "Mount Fuji — Japan",
            "image": "https://upload.wikimedia.org/wikipedia/commons/1/12/Mount_Fuji_from_Lake_Kawaguchi.jpg"
        }
    ]

    index_value = int(request.GET.get("index", 0))
    index_value = index_value % len(data)

    context = {
        "item": data[index_value],
        "next_index": (index_value + 1) % len(data),
        "prev_index": (index_value - 1 + len(data)) % len(data),
    }

    return render(request, "header.html", context)