def meet_in_middle_attack_pairs(pairs):
            
            start_time = time.time()

            first_pt, first_ct = pairs[0]
            mid_dict = {}  # using a dictionary to store list of K1 keys producing intermediate state
            candidates = []

            # forward encryption with all potential k1 values
            for k1_val in range(1024):  # 0 to 1023
                key1 = bs.Bits(uint=k1_val, length=10)
                mid = sdes_encrypt(first_pt, key1)

                if mid in mid_dict: # store potential k1's in dictionary
                    mid_dict[mid].append(key1)

                else:
                    mid_dict[mid] = [key1]


            
            for k2_val in range(1024): # reverse decryption with all possible k2 values
                key2 = bs.Bits(uint=k2_val, length=10)
                mid_val = sdes_decrypt(first_ct, key2)

                if mid_val in mid_dict:
                    key1_list = mid_dict[mid_val]  # get matching k1s

                    for candidate_key1 in key1_list:
                        candidates.append((candidate_key1, key2))



            for pair in candidates:     # verify candidates against all known pairs
                key1, key2 = pair
                valid = True  # flag for valid keys

                for pt, ct in pairs:
                    if dsdes_encrypt(pt, key1, key2) != ct:
                        valid = False
                        break  # break if invalid

                if valid:
                    end_time = time.time()
                    total = end_time - start_time
                    print("Attack took", total, "seconds")
                    return key1, key2  # return key pair


            end_time = time.time()
            print("no valid keys")

            return bs.Bits(bin="0000000000"), bs.Bits(bin="0000000000")  # return 0 keys if nothing found


    


        def main():
        # main function to be called in proj1.py
       
        pairs = [
            (bs.Bits(hex="42"), bs.Bits(hex="0f")),
            (bs.Bits(hex="72"), bs.Bits(hex="85")),
            (bs.Bits(hex="75"), bs.Bits(hex="3b")),
            (bs.Bits(hex="74"), bs.Bits(hex="2e")),
            (bs.Bits(hex="65"), bs.Bits(hex="ed"))
        ]
        
        # meet in middle attack
        k1, k2 = meet_in_middle_attack_pairs(pairs)
        
        print("Keys Found! K1: ", k1.bin, "K2: ", k2.bin)
