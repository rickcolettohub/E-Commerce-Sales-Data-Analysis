from rapidfuzz import fuzz, process


def check_misspell(mispell_list: list[str], correspondent_list: list[str], weight: int = 90):
    corrections = {}

    for mispell in mispell_list:
        match, score, idx_ = process.extractOne(
            mispell, correspondent_list, scorer=fuzz.ratio)
        if match:  # evita erro caso não encontre nada
            matched_str, score = match
            if score >= weight:
                corrections[mispell] = matched_str

    return corrections
