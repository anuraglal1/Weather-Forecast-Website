def weatherTest():
  r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=01d1f6ccaffe5c8f36a6196d7c7485a6')
  json_object = r.json()
  exptected = r.getTemp();
  actual = 35
  assertTrue(exptected, actual)
