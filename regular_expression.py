# Author: Tom, Lexica
# given regular expression, which of the following will match?

r"((?:(?:\bNN.?_(?:.+?))(.*?)(?:\bVB.?_(?:.+?)))|(?:(?:\bVB.?_(?:.+?))(.*?)(?:\bNN.?_(?:.+?)))|WRB_(?:.+?))\b([A-Z]{2,}_(?:so) [A-Z]{2,}_(?:that)|([A-Z]{2,}_(?:as) [A-Z]{2,}_(?:long|soon|early) [A-Z]{2,}_(?:as))|(?:[A-Z]{2,}_(?:while|where|as|however|and|but|or|yet)))\b(?:.*?)((?:(?:\bNN.?_(?:.+?))(.*?)(?:\bVB.?_(?:.+?)))|(?:(?:\bVB.?_(?:.+?))(.*?)(?:\bNN.?_(?:.+?)))|WRB_(?:.+?))"


1. PRP_I MD_would VB_like TO_to VB_know WRB_where VBP_are PRP_they JJ_located IN_as PRP_I VBP_need PRP_them IN_for PRP$_my NN_course
2. PRP_I MD_would VB_like TO_to VB_know WRB_where MD_can PRP_I VB_find NN_book
3. PRP_I VBP_am VBG_looking IN_for DT_a NN_book WRB_where PRP_it MD_can RB_not VB_be VBN_found
4. VBZ_is PRP_it JJ_possible TO_to VB_find DT_this NN_book CC_and WRB_where TO_to VB_find PRP_it