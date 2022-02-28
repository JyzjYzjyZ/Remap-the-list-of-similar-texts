# Remap-the-list-of-similar-texts
<h2>Description</h2>
You can enter a definite and correct string, and a list that is not perfect but sufficient as a reference. Output the new list after remapping. For subtitle timeline 

你可以输入一个确定且正确的字符串，和一个不完美但足够作为参照的列表。输出重映射后的新列表。用于字幕时间轴 

input:
···
sentences = ['GEISON WILL COME TO THE NEXT PART OF THE SERIES TO DHO WORK I BE TALKING ABOUT THE INTRFACE AND BELIEVE ME IT IS A TRICKER ONE SO', 'WELCOME TO THE INTERFASE SEMERS IS FAMOUS FOR HAVING ONE OF IVNOT THE WORST INTERFACES INTO TRETY WORLD', 'AND ONE OF THE RECENCES THE GUISE THAT INITIALLY BUILT CIBERT THEY WERE NOT USED LIKE INTERPHASE THE SIGNERS THEY WERE JUST PROGRAMMERS WRITE SO', "THEY TRIED THEIR BEST AND THEY CREATED THIS WHICH IS NOT BAD IT'S NOT BAD BUT IT GETS A LITTLE BIT CONFUSING SO", 'THE SCHOOL']
punctuate = "M GUIS, AN WELCOME TO THE NEXT PART OF THE SERIES. TO DAY, WORKANA BE TALKING ABOUT THE INTERFHACE AND, BELIEVE ME, IT IS A TRICKY ONE. SO AWELCOME TO THE INTERFHASE. SEBERS IS FAMOUS FOR HAVING ONE OF IFNOT THE WORST INTERFHACES INTHO TREEDY WORLD AND ONE OF THE RECENCIS THAT THE GUISE TAD INITIALLY BUILT SEBER. THEY WERE NOT USED, LIKE INTERFHASE A SIGNERS. THEY WERE JUST PROGRAMMERS WRITE. SO THEY TRIED THEIR BEST AND THEY CREATED THIS, WHICH ITS NOT BAD. IT'S NOT BAD BUT IT GETS A LITTLE BIT CONFUSING. SO LET'S GO."
···

output[list]:
```
M GUIS,
AN WELCOME TO THE NEXT PART OF THE SERIES.TO DAY,WORKANA BE TALKING ABOUT THE INTERFHACE AND,BELIEVE ME,
IT IS A TRICKY ONE.SO AWELCOME TO THE INTERFHASE.SEBERS IS FAMOUS FOR HAVING ONE OF IFNOT THE WORST INTERFHACES INTHO TREEDY WORLD AND ONE OF THE RECENCIS THAT THE GUISE TAD INITIALLY BUILT SEBER.THEY WERE NOT USED,LIKE INTERFHASE A SIGNERS.THEY WERE JUST PROGRAMMERS WRITE.
SO THEY TRIED THEIR BEST AND THEY CREATED THIS,WHICH ITS NOT BAD.
IT'S NOT BAD BUT IT GETS A LITTLE BIT CONFUSING.SO LET'S GO.
```

<h2>installed </h2>
```
import copy
import gc
import re
import warnings
import Levenshtein
```
If you fail to install using pip, try conda

Calling the main function, debugBool means whether to output additional content or not. The filter function defines what differences in the matched elements will be accepted, e.g. how much of the same word same will be considered invalid when separated by a base value. Usually constant value functions are used

调用main函数，debugBool意味着是否输出额外的内容。过滤器函数定义比配元素的何种差异能被接受，列如相同的单词same相隔基准值多少会被视为无效值。通常使用常值函数

<h3 style="color:red">!!!</h3>
Under development for very different, or overly stringent filter functions. Cannot provide good support

正在开发非常不同的，或过于严格的过滤器函数。不能提供良好的支持
