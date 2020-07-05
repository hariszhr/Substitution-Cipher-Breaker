from Common import *
import collections

def Start_Algorithm (input_ciphertext, num_of_iterations, real_key):
    real_key=real_key.upper()
    MAX_NUM_OF_INIT_KEY_ITERATIONS = num_of_iterations
    E=''  # expected bigram
    D=''  # stored bigram
    _D='' # current bigram
    v=''  # stored score
    _v='' # current scrore
    k=''  # stored key
    _k='' # current key

    # ******* STEP 1: construct initial key guess , k, based upon symbol frequencies of the expected language and the cipher text
    ciphertext = clean_up(input_ciphertext)

    text_From_book = clean_up(getTextFromBook())

    print("ciphertext",ciphertext)
    print("cipher text size: ",len(ciphertext))
    print('Character count from file: ', len(text_From_book))

    # CREATING REFERENCE FREQUENCY LIST AND REFERENCE BIGRAM
    print('book frequency list: ')
    book_freq_char_list, book_freq_count_list = getFrequencyCounts(text_From_book)

    # CREATING CIPHER TEXT FREQUENCY LIST
    print('ciphertext frequency list: ')
    ct_freq_char_list, ci_freq_list = getFrequencyCounts(ciphertext)

    initial_key_dict = collections.OrderedDict()
    for n in range(26):
        initial_key_dict[book_freq_char_list[n]]=ct_freq_char_list[n]

    k = initial_key_dict.copy()
    print('initial key: ',k)

    # ******* STEP 1 - END **********************************************************

    # ******* STEP 2: generate expected bigram and ciphertext bigram
    book_bigram = getBigram(text_From_book, book_freq_char_list)
    E = book_bigram.copy()

    ct_bigram = getBigram(ciphertext, ct_freq_char_list)
    D=ct_bigram.copy()
    # ******* STEP 2 - END **********************************************************

    # ******* STEP 3: INITIAL SCORE
    v = numpy.sum(numpy.abs(D - E))
    print('initial key\'s bigram score: ',v)
    # ******* STEP 3 - END **********************************************************

    # ******* STEP 4: assign values to current variables
    _k = k.copy()
    _v = v
    _D = D.copy()
    # ******* STEP 4 - END **********************************************************

    # ******* STEP 5: LOOP
    a,b=0,0
    for idx in range(MAX_NUM_OF_INIT_KEY_ITERATIONS):
        for i in range(26):
            a = -1
            b = i
            for j in range(26):
                a += 1
                b += 1
                if(b>25):
                    break

                # swap key
                tiger=list(_k.keys())
                _temp=_k[tiger[a]]
                _k[tiger[a]]=_k[tiger[b]]
                _k[tiger[b]] = _temp
                # print('swap',a,b)
                # print('stored key:', k)
                # print('new key   :',_k)

                # swap bigram row
                tempRow = numpy.copy(_D[a, :])
                _D[a, :] = _D[b, :]
                _D[b, :] = tempRow

                # replace columns
                tempCol = numpy.copy(_D[:, a])
                _D[:, a] = _D[:, b]
                _D[:, b] = tempCol

                _v = numpy.sum(numpy.abs(_D - E))

                if _v < v:
                    print('better score found: ',_v)
                    v = _v
                    k = _k.copy()
                    D = _D.copy()
                else:
                    _k = k.copy()
                    _D = D.copy()
    # ******* STEP 5 - LOOP END **********************************************************
    print('final bigram score:',v)

    aa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    norm_k = ''
    for c in aa:
        norm_k = norm_k+k[c]
    print('final key:',norm_k)
    print('true key :',real_key)

    # Calculate key match
    if real_key.strip() is not '':
        match_count = 0
        for i in range(26):
            if (norm_k[i] is real_key[i]):
                match_count += 1
        key_match = (match_count / 26) * 100
        print('key match: ', key_match, '%')
    else:
        key_match = ''

    # retrieve plain text from final key
    final_plain_text = ''
    _keys_list= list(k.keys())
    _values_list = list(k.values())
    for c in ciphertext:
        idx = _values_list.index(c)
        final_plain_text = final_plain_text + _keys_list[idx]
    # print("cipher text:                 " + ciphertext)
    # print("plain text with final key:   " + final_plain_text)
    return final_plain_text, norm_k, str(key_match)


