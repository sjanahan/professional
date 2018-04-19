# 0. Prompt

1. Reverse the letters in each word without reversing the order of the words
    1. Write a function to reverse the letters.  Do not use a built-in function.
2. Replace digits with the spelling of those digits
    1. All non-digit characters should be treated like letters.
    2. When numbers have letters attached (such as "21st"), treat the numbers as if they were letters.  For example, "21st" becomes "ts12"
    
Extra Credit
1. Reverse the process!  Write a function that takes the output of the previous class and returns it to its original form.

# 1. Resolve ambiguity
1. Do the numbers have to be standalone to be converted? Yes
2. What happens with an empty string? Nothing.
3. Will there be multiple whitespaces? No

# 2. Example
|Input | Output|
|---   | ---   | 
|Captain Piccard just zapped 51 Romulan ships! | niatpaC dracciP tsuj deppaz one five nalumoR !spihs
|Data’s brother Lore has an emotion chip and 100 petabytes of RAM | s’ataD rehtorb eroL sah na noitome pihc dna zero zero one setybatep fo .MAR|
|"I believe he’s lying," said Deanna Troi to 1st Officer Riker| I" eveileb s’eh ",gniyl dias annaeD iorT ot ts1 reciffO .rekiR |

# 3. Brute Force
1. Reverse the letters in each word without reversing the order of the words
    1. Split the string by whitespace into a list
    2. For each item in the list, reverse the characters in it
2. Replace digits with the spelling of those digits
    1. For each item in the list, if it matches a regex '^[0-9]+$'
        1. If it does, do a lookup in the {digit : english repr} dict and concatenate
        
# 4. Time and Space Analysis
1. Time: O(l) where l is number of letters

   Space: O(w) where w is number of words

2. Time: O(w) where w is number of words

   Space: O(1) constant for lookup table. Potentially could be big if there's a large number

#5. Walk through it

#6. Code it

#7. Test


