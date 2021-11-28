import nltk

print('')
print('Zadanie 13: Zdefiniować funkcję, która dla zadanego zdania wyszukuje 3-gramy pasujące do wzorca czasownik+TO+czasownik. Przetestować na 5 wybranych przykładach.')
print('')


def find_trigram(text):
    sentences = nltk.sent_tokenize(text)
    trigram_phrases = []

    for sentence in sentences:
        tagged_sentence = nltk.pos_tag(nltk.word_tokenize(sentence), tagset='universal')

        for (word_one, tag_one), (word_two, tag_two), (word_three, tag_three) in nltk.trigrams(tagged_sentence):
            if (tag_one == 'VERB' and word_two.lower() == 'to' and tag_three == 'VERB'):
                found_trigram = word_one + ' ' + word_two + ' ' + word_three
                trigram_phrases.append(str.lower(found_trigram))

    if len(trigram_phrases):
        print('Trigrams "VERB + to + VERB":')
        for trigram_phrase in trigram_phrases:
            print(trigram_phrase)
    else:
        print('Trigrams "VERB + to + VERB" not found.')


text_example_1  = """Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice “without pictures or conversations?”
So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.
There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, “Oh dear! Oh dear! I shall be late!” (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge."""

text_example_2 = """ A gentleman friend and I were dining at the Ritz last evening and he
said that if I took a pencil and a paper and put down all of my
thoughts it would make a book. This almost made me smile as what it
would really make would be a whole row of encyclopediacs. I mean I seem
to be thinking practically all of the time. I mean it is my favorite
recreation and sometimes I sit for hours and do not seem to do anything
else but think. So this gentleman said a girl with brains ought to do
something else with them besides think. And he said he ought to know
brains when he sees them, because he is in the senate and he spends
quite a great deal of time in Washington, d. c., and when he comes into
contract with brains he always notices it. So it might have all blown
over but this morning he sent me a book. And so when my maid brought it
to me, I said to her, “Well, Lulu, here is another book and we have not
read half the ones we have got yet.” But when I opened it and saw that
it was all a blank I remembered what my gentleman acquaintance said,
and so then I realized that it was a diary. So here I am writing a book
instead of reading one.

But now it is the 16th of March and of course it is to late to begin
with January, but it does not matter as my gentleman friend, Mr.
Eisman, was in town practically all of January and February, and when
he is in town one day seems to be practically the same as the next day."""

text_example_3 = """MARLEY was dead: to begin with. There is no doubt
whatever about that. The register of his burial was
signed by the clergyman, the clerk, the undertaker,
and the chief mourner. Scrooge signed it: and
Scrooge's name was good upon 'Change, for anything he
chose to put his hand to. Old Marley was as dead as a
door-nail.

Mind! I don't mean to say that I know, of my
own knowledge, what there is particularly dead about
a door-nail. I might have been inclined, myself, to
regard a coffin-nail as the deadest piece of ironmongery
in the trade. But the wisdom of our ancestors
is in the simile; and my unhallowed hands
shall not disturb it, or the Country's done for. You
will therefore permit me to repeat, emphatically, that
Marley was as dead as a door-nail.

Scrooge knew he was dead? Of course he did.
How could it be otherwise? Scrooge and he were
partners for I don't know how many years. Scrooge
was his sole executor, his sole administrator, his sole
assign, his sole residuary legatee, his sole friend, and
sole mourner. And even Scrooge was not so dreadfully
cut up by the sad event, but that he was an excellent
man of business on the very day of the funeral,
and solemnised it with an undoubted bargain."""

text_example_4 = """Mrs Dalloway said she would buy the gloves herself.

Big Ben was striking as she stepped out into the street. It was eleven
o'clock and the unused hour was fresh as if issued to children on a
beach. But there was something solemn in the deliberate swing of the
repeated strokes; something stirring in the murmur of wheels and the
shuffle of footsteps.

No doubt they were not all bound on errands of happiness. There is much
more to be said about us than that we walk the streets of Westminster.
Big Ben too is nothing but steel rods consumed by rust were it not for
the care of H. M.'s Office of Works. Only for Mrs Dalloway the moment
was complete; for Mrs Dalloway June was fresh. A happy childhood--and it
was not to his daughters only that Justin Parry had seemed a fine fellow
(weak of course on the Bench); flowers at evening, smoke rising; the caw
of rooks falling from ever so high, down down through the October
air--there is nothing to take the place of childhood. A leaf of mint
brings it back; or a cup with a blue ring.

Poor little wretches, she sighed, and pressed forward. Oh, right under
the horses' noses, you little demon! and there she was left on the kerb
stretching her hand out, while Jimmy Dawes grinned on the further side.

A charming woman, poised, eager, strangely white-haired for her pink
cheeks, so Scope Purvis, C. B., saw her as he hurried to his office. She
stiffened a little, waiting for Durtnall's van to pass. Big Ben struck
the tenth; struck the eleventh stroke. The leaden circles dissolved in
the air. Pride held her erect, inheriting, handing on, acquainted with
discipline and with suffering. How people suffered, how they suffered,
she thought, thinking of Mrs Foxcroft at the Embassy last night decked
with jewels, eating her heart out, because that nice boy was dead, and
now the old Manor House (Durtnall's van passed) must go to a cousin.
"""

text_example_5 = """My neighbor V.N.S. told me that his uncle Fet-Shenshin, the famous
poet, when driving through the Mokhovaia Street, would invariably let
down the window of his carriage and spit at the University. He would
expectorate and spit: Bah! His coachman got so used to this that every
time he drove past the University, he would stop.

In January I was in Petersburg and stayed with Souvorin. I often
saw Potapenko. Met Korolenko. I often went to the Maly Theatre.
As Alexander [Chekhov's brother] came downstairs one day, B.V.G.
simultaneously came out of the editorial office of the _Novoye
Vremya_ and said to me indignantly: "Why do you set the old man
(i.e. Souvorin) against Burenin?" I have never spoken ill of the
contributors to the _Novoye Vremya_ in Souvorin's presence, although I
have the deepest disrespect for the majority of them.

In February, passing through Moscow, I went to see L.N. Tolstoi. He
was irritated, made stinging remarks about the _décadents_, and for
an hour and a half argued with B. Tchitcherin, who, I thought, talked
nonsense all the time. Tatyana and Mary [Tolstoi's daughters] laid
out a patience; they both wished, and asked me to pick a card out;
I picked out the ace of spades separately for each of them, and that
annoyed them. By accident there were two aces of spades in the pack.
Both of them are extraordinarily sympathetic, and their attitude to
their father is touching. The countess denounced the painter Gé all
the evening. She too was irritated.
"""

print(find_trigram(text_example_1), '\n')
print(find_trigram(text_example_2), '\n')
print(find_trigram(text_example_3), '\n')
print(find_trigram(text_example_4), '\n')
print(find_trigram(text_example_5), '\n')