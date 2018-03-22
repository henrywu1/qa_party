response = {
  "code":200,
  "pagination": None,
  "data":{
    "Week of 04/02/18":[
      "Invalid! Not all Lotteries open and close at the same time.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX AM, picking starts XXXX-XX-XX XX:XX AM & ends XXXX-XX-XX XX:XX AM.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX AM, picking starts XXXX-XX-XX XX:XX AM & ends XXXX-XX-XX XX:XX PM.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX AM, picking starts XXXX-XX-XX XX:XX AM & ends XXXX-XX-XX XX:XX AM.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX AM, picking starts XXXX-XX-XX XX:XX AM & ends XXXX-XX-XX XX:XX AM."
    ],
    "Week of 02/19/18":[
      "Invalid! Not all Lotteries open and close at the same time.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX PM, picking starts XXXX-XX-XX XX:XX PM & ends XXXX-XX-XX XX:XX PM.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX PM, picking starts XXXX-XX-XX XX:XX PM & ends XXXX-XX-XX XX:XX PM.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX PM, picking starts XXXX-XX-XX XX:XX PM & ends XXXX-XX-XX XX:XX PM."
    ],
    "Week of Feb 12, 2018":[
      "Invalid! Not all showtimes have Lottery XXXXXallocations.",
      "AllocatedShowtime 312321 (XXXX-XX-XX XX:XX PM) is missing Lottery XXXXXallocations.",
      "AllocatedShowtime 312317 (XXXX-XX-XX XX:XX PM) is missing Lottery XXXXXallocations.",
      "AllocatedShowtime 312318 (XXXX-XX-XX XX:XX PM) is missing Lottery XXXXXallocations."
    ],
    "Week of 03/12/18":[
      "Invalid! Not all Lotteries open and close at the same time.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX AM, picking starts XXXX-XX-XX XX:XX PM & ends XXXX-XX-XX XX:XX PM.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX AM, picking starts XXXX-XX-XX XX:XX PM & ends XXXX-XX-XX XX:XX PM.",
      "Lottery XXXXX (XXXX-XX-XX XX:XX PM) opens XXXX-XX-XX XX:XX AM, picking starts XXXX-XX-XX XX:XX PM & ends XXXX-XX-XX XX:XX PM."
    ],
    "Week of 03/henry/18":[
      "Invalid! Not all showtimes have Lottery XXXXXallocations.",
      "AllocatedShowtime 312322 (XXXX-XX-XX XX:XX PM) is missing Lottery XXXXXallocations.",
      "AllocatedShowtime 312985 (XXXX-XX-XX XX:XX PM) is missing Lottery XXXXXallocations.",
      "AllocatedShowtime 312792 (XXXX-XX-XX XX:XX PM) is missing Lottery XXXXXallocations.",
      "AllocatedShowtime 312761 (XXXX-XX-XX XX:XX PM) is missing Lottery XXXXXallocations."
    ]
  },
}



for week_title, array_of_info in response['data'].items():
    print week_title
    for string in array_of_info:
        print string
    print
