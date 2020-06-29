def total_device_energy(data):
    clientprop = ClientProperties()
    area_desktop = 0.24 #average desktop size approximately 60cmx40cm

    #lifetimes given in hours
    lifetime = {'laptop': 35040, 'desktop' : 35040, 'LED screen': 100000, 'Plasma screen': 45000, 'High performance codec': 87600, 'Low performance codec': 87600, 'Camera': 70080, 'Speaker' : 17520, 'Microphone' : 175200, 'Router' : 30660}
    energy = 0
    hours = data['Hours']
    operating_seconds = hours * 360
    # operating energy = power in watts * seconds
    #energy from manufacturing = total manufacturing energy * hours used / lifetime

    # add energy from the laptops
    energy += data['Number of laptops'] * clientprop.laptop.power * operating_seconds
    energy += data['Number of laptops'] * clientprop.laptop.manufacture_energy * hours/lifetime['laptop']

    # add energy from the desktops
    energy += data['Number of desktops'] * clientprop.personal_comp.power * operating_seconds
    energy += data['Number of desktops'] * clientprop.personal_comp.manufacture_energy * hours/lifetime['desktop']

    # add energy from the desktop screens
    energy += data['Number of desktops'] * (data['Percentage LED and LCD']/100) * clientprop.ledlcd(area_desktop).power
    energy += data['Number of desktops'] * (data['Percentage LED and LCD']/100) * clientprop.ledlcd(area_desktop).manufacture_energy * hours/lifetime['LED screen']

    energy += data['Number of desktops'] * ((100 - data['Percentage LED and LCD'])/100) * clientprop.plasma(area).power
    energy += data['Number of desktops'] * ((100 - data['Percentage LED and LCD'])/100) * clientprop.plasma(area).manufacture_energy * hours/lifetime['Plasma screen']

    # add energy from extra screens

    energy += data['Number of extra LCD/LED screens'] * clientprop.ledlcd(data['Area of extra LED/LCD screens']).power
    energy += data['Number of extra LCD/LED screens'] * clientprop.ledlcd(data['Area of extra LED/LCD screens']).manufacture_energy * hours/lifetime['LED screen']

    energy += data['Number of extra plasma screens'] * clientprop.ledlcd(data['Area of extra LED/LCD screens']).power
    energy += data['Number of extra plasma screens'] * clientprop.ledlcd(data['Area of extra plasma screens']).manufacture_energy * hours/lifetime['Plasma screen']

    # add energy from CODECs
    energy += data['Number of high performance CODECs'] * clientprop.high_codec.power * operating_seconds
    energy += data['Number of high performance CODECs'] * clientprop.high_codec.manufacture_energy * hours/lifetime['High performance codec']

    energy += data['Number of low performance CODECs'] * clientprop.low_codec.power * operating_seconds
    energy += data['Number of low performance CODECs'] * clientprop.low_codec.manufacture_energy * hours/lifetime['Low performance codec']

    # add operating energy from cameras, speakers, microphones and routers
    energy += data['Number of cameras'] * clientprop.camera.power * operating_seconds
    energy += data['Number of speakers'] * clientprop.speaker.power * operating_seconds
    energy += data['Number of microphones'] * clientprop.microphone.power * operating_seconds
    energy += data['Number of routers'] * clientprop.router.power * operating_seconds

    # add manufacturing energy from cameras, speakers, microphones and routers
    energy += data['Number of cameras'] * clientprop.camera.manufacture_energy * hours/lifetime['Camera']
    energy += data['Number of speakers'] * clientprop.speaker.manufacture_energy * hours/lifetime['Speaker']
    energy += data['Number of microphones'] * clientprop.microphone.manufacture_energy * hours/lifetime['Microphone']
    energy += data['Number of routers'] * clientprop.router.manufacture_energy * hours/lifetime['Router']

    return energy


def mainfun():
    print("Enter the number of hours over which the video conference will take place")
    hours=int(input())
    print('How many PCs will be used in the video conference?')
    num_pcs = int(input())
    print('Approximately what percentage of these are desktops? (Enter u for unknown)')
    percent_desktop =input()
    if(percent_desktop=='u'):
        percent_desktop=57.1
    num_desktops = num_pcs * int(percent_desktop)/100
    num_laptops = num_pcs - num_desktops
    print('What percentage of these desktops use LED or LCD screens (Enter u for unknown)')
    per_LED=input()
    if (per_LED=='u'):
        per_LED=78.6#global average of LED or LCD screens
    print('How many additional LCD/LED screens are being used?')
    extra_led = int(input())
    print('How big are these screens (inches)? Enter u for unknown')
    width_led = input()
    if width_led == 'u':
        width_led = 60
    width_led = int(width_led)

    #most TV displays have aspect ratio 16:9
    height_led = (width_led/16) * 9
    area_led = width_led * height_led
    area_led *= 0.00064516 #convert to metre squared
    print('How many additional plasma screens are being used?')
    extra_plasma = int(input())
    print('How big are these screens (inches)? Enter u for unknown')
    width_plasma = input()
    if width_plasma == 'u':
        width_plasma = 60
    #most TV displays have aspect ratio 16:9
    width_plasma = int(width_plasma)
    height_plasma = (width_plasma/16) * 9
    area_plasma = width_plasma * height_plasma
    area_plasma *= 0.00064516 #convert to metre squared
    print('Number of High end CODECs used ')
    num_high_codecs= int(input())
    print('Number of Low end CODECs used ')
    num_low_codecs= int(input())
    print('Number of cameras used ')
    num_cameras= int(input())
    print('Number of speakers used ')
    num_speakers= int(input())
    print('Number of microphones used ')
    num_microphones= int(input())
    print('Number of routers used ')
    num_routers= int(input())
    data={'Hours':hours, 'Number of desktops':num_desktops, 'Number of laptops':num_laptops, 'Percentage LED and LCD':int(per_LED), 'Number of extra LCD/LED screens':extra_led, 'Area of extra LED/LCD screens':area_led, 'Number of extra plasma screens':extra_plasma, 'Area of extra plasma screens':area_plasma, 'Number of high performance CODECs':num_high_codecs, 'Number of low performance CODECs':num_low_codecs, 'Number of cameras':num_cameras, 'Number of speakers':num_speakers, 'Number of microphones':num_microphones, 'Number of routers':num_routers}              
    print(data)
    return data
data = mainfun()
energy = total_device_energy(data)
print(energy)
