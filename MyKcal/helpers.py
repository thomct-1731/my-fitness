def getMacrosData(calories_day):
  return [
    {
      'name': 'Moderate Carb (30/35/35)',
      'protein': round((calories_day*0.3)/4),
      'fats': round((calories_day*0.35)/9),
      'carbs': round((calories_day*0.35)/4),
      'explain': '30/35/35 = 30% protein, 35% fats, 35% carbs'
    },
    {
      'name': 'Lower Carb (40/40/20)',
      'protein': round((calories_day*0.4)/4),
      'fats': round((calories_day*0.4)/9),
      'carbs': round((calories_day*0.2)/4),
      'explain': '40/40/20 = 40% protein, 40% fats, 20% carbs'
    },
    {
      'name': 'Higher Carb (30/20/50)',
      'protein': round((calories_day*0.3)/4),
      'fats': round((calories_day*0.2)/9),
      'carbs': round((calories_day*0.5)/4),
      'explain': '30/20/50 = 30% protein, 20% fats, 50% carbs'
    }
  ]
