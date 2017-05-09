OP_BR, CL_BR = '(', ')'
class RemovingParenthesis:
    def countWays(self, s):
        return self.countPrs(s)

    def get_first_valid_close(self, prnths):
        opening_brackets = 0
        closing_brackets = 0
        for idx, br in enumerate(prnths):
            if br == OP_BR:
                opening_brackets += 1
            elif br == CL_BR:
                if opening_brackets <= closing_brackets:
                    # Closing a non-existing bracket, wtf
                    return False
                closing_brackets += 1
                if opening_brackets == closing_brackets:
                    return idx
        return opening_brackets == closing_brackets

    def countPrs(self, pars, multiplier=1):
        if len(pars) == 0:
            return 1
        closing_bracket_idx = self.get_first_valid_close(pars)
        return multiplier * self.countPrs(pars[1:closing_bracket_idx], multiplier + 1) * self.countPrs(
            pars[closing_bracket_idx + 1:], multiplier)

