from openai import OpenAI

sample_emails = [
    "Subject: Printing Issue\n\nHi Team,\n\nI've noticed an issue with the office printer. John was trying to print some documents but the printer jammed. Can someone look into it?\n\nThanks,\nJane",
    "Subject: Printing Schedule\n\nHello,\n\nJust a reminder that Sarah will be printing the monthly reports tomorrow morning. Please avoid using the printer during this time.\n\nBest,\nTom",
    "Subject: Urgent Printing Request\n\nDear All,\n\nI need to print some contracts for our meeting this afternoon. Can you please ensure the printer is available at 2 PM? Thanks in advance.\n\nRegards,\nDavid",
    "Subject: Printer Maintenance\n\nHi Everyone,\n\nPlease note that the printer will be undergoing maintenance this Friday. Karen is handling the last batch of print jobs today. Plan accordingly.\n\nCheers,\nMike",
    "Subject: Printing Paper Shortage\n\nTeam,\n\nWe are running low on printing paper. Emily was the last to print and mentioned the paper is almost out. I'll order more supplies today.\n\nRegards,\nAlex",
    "Subject: Double-Sided Printing\n\nHello All,\n\nTo save paper, please set your print jobs to double-sided. Mark was printing earlier and used up quite a bit of paper. Let's be mindful of our usage.\n\nThanks,\nSophie",
    "Subject: Print Job Error\n\nHi IT,\n\nI'm having trouble with a print job. Steven tried printing his presentation but it didn't come out correctly. Could someone assist?\n\nBest,\nLucy",
    "Subject: Printing Costs\n\nDear Team,\n\nWe've noticed an increase in printing costs. Paul has been printing large volumes for the upcoming project. Let's try to print only what's necessary.\n\nThanks,\nRachel",
    "Subject: Color Printing\n\nHi All,\n\nRemember to use the color printer only when necessary. Alice printed a bunch of color brochures today. Let's conserve color ink for essential tasks.\n\nRegards,\nJames",
    "Subject: Printer Usage Etiquette\n\nHello Team,\n\nPlease be considerate when printing. Ben was printing multiple copies of his report and it delayed others. Let's ensure fair usage of the printer.\n\nThanks,\nEmma"
]

api_key = ""
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)
