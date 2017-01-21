# AC-FreeC
Auto reminder for when you should close the window in the summer when you've got no AC.

The script helps you to cool down your appartment in the summer when you've got no automatic air conditioning system. You open the windows in the morning when it's (hopefully) still a bit cooler. The script then compares outside temperature to an indoor temperature provided by you that shouldn't be exceeded. It messages you when either the outside temperature reaches the critical level or when other factors (e.g. rain) may force you to close the windows. 

## How to Use
1. install the dependencies:
```pip install -r requirements.txt```

2. Set up accounts with *twilio* and *OpenWeatherMap*

3. Add your information to "textmyself.py" (twilio) and "acfreec.py" (OpenWeatherMap)

4. For this to be useful, you might want to set up the script in a way that it runs automatically every half hour or so.

## To Do
- [ ] Add timing feature so that people who don't know how to do #4 can start and stop it manually, and it'll keep checking every half hour inbetween

# 
*__Please Note__: my free trial account expired, so I can't test this anymore for the time being.*
