import re

class StringReverser:
  lookup = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
  }


  def reverse_word(self, word):
    start = 0
    end = len(word)
    midpoint = int((start+end)/2)
    l = list(word)

    for i in range(0, midpoint):
      front = i
      back = end-1-i
      l[front], l[back] = l[back], l[front]

    return "".join(l)


  def replace_digits_with_english(self, word):
    regex = re.compile('^[0-9]+$')
    new_word = word

    if re.match(regex, word) is not None:
      new_word = []
      for n in word:
        new_word.append(StringReverser.lookup[int(n)])

      new_word = " ".join(new_word)

    return new_word


  def do_reverse(self, str):
    # error checking
    if str is None or str == '':
      return str

    items = str.split(" ")
    reversed_words = []
    for item in items:
      reversed_word = self.reverse_word(item)
      numbers_replaced_word = self.replace_digits_with_english(reversed_word)
      reversed_words.append(numbers_replaced_word)

    return " ".join(reversed_words)

class TestRunner:
  cases = [
    {
      "input": "Captain Piccard just zapped 51 Romulan ships!",
      "output": "niatpaC dracciP tsuj deppaz one five nalumoR !spihs"
    },
    {
      "input": "Data's brother Lore has an emotion chip and 100 petabytes of RAM.",
      "output": "s'ataD rehtorb eroL sah na noitome pihc dna zero zero one setybatep fo .MAR"
    },
    {
      "input": "\"I believe he's lying,\" said Deanna Troi to 1st Officer Riker.",
      "output": "I\" eveileb s'eh \",gniyl dias annaeD iorT ot ts1 reciffO .rekiR"
    }
  ]
  def __init__(self):
    self.reverser = StringReverser()

  def run_test_cases(self):
    incorrect_cases = 0
    for case in self.cases:
      reverser_output = self.reverser.do_reverse(case['input'])
      if reverser_output != case['output']:
        incorrect_cases += 1
        print("Incorrect result :")
        print("Input : " + case['input'])
        print("Correct output : " + case['output'])
        print("Reverser output : " + reverser_output)

    if incorrect_cases == 0:
      print("Success! All test cases passed")
    else:
      print("Failure! %d cases failed" % incorrect_cases)

tr = TestRunner()
tr.run_test_cases()
