

def nilai(nilai):
    if nilai < 60:
        return "Gagal"
    elif 60 < nilai <= 70:
        return "Baik"
    elif 70 < nilai <= 80:
        return "Sangat Baik"
    elif 80 < nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"
    
