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

    last_index = len(data) - 1
    try:
        current_index = int(request.GET.get("index", 0))
    except (TypeError, ValueError):
        current_index = 0

    # Clamp current_index to valid range [0, last_index]
    current_index = max(0, min(current_index, last_index))

    # Determine previous and next indices safely
    prev_index = max(current_index - 1, 0)
    next_index = min(current_index + 1, last_index)

    context = {
        "item": data[current_index],
        "current_index": current_index,
        "prev_index": prev_index,
        "next_index": next_index,
        "last_index": last_index,
    }

    return render(request, "header.html", context)