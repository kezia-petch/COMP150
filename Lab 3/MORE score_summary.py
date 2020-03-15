def score_summary(name, x, y, z):
    print(name, "-", "Max:", max(x, y, z), ",", "Min:", min(x, y, z), ",", "Average:", (x+y+z)/3)
    
score_summary("Fred", 3, 4, 5)