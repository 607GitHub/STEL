import set_for_global
set_for_global.set_logging()


def test_contraction_generation():
    from generate_pot_quads import main
    main(action="generate-char-quads", style_char=[set_for_global.CONTRACTION])


def test_nsubs_generation():
    from generate_pot_quads import main
    main(action="generate-char-quads", style_char=[set_for_global.NBR_SUBSTITUTION])

def test_emotive_generation():
    from generate_pot_quads import main
    main(action="generate-char-quads", style_char=[set_for_global.EMOTIVE])

def test_gen_subsposs():
    import nsubs_possibilities
    import to_add_const

    NPoss = nsubs_possibilities.NumberSubsPossibilities(total=100000, pushshift_month=to_add_const.PUSHSHIFT_MONTH_6)
    NPoss._init_style_sentences()
