from typing import List


class BasicNeeds:
    def __init__(self, debug: bool = False) -> None:
        self.debug = debug

    def assess_blocks(self, blocks: List[dict], requirements: List[str]) -> int:
        ########################################################################
        # DO NOT DO THE FOLLOWING... it will yield unexpected behaviors...
        # REF: https: // stackoverflow.com / questions / 2397141 / how - to - initialize - a - two - dimensional - array - in -python
        # requirement_scores = [[-1] * len(requirements)] * len(blocks) << CRAZY SHIT HAPPENS
        ########################################################################
        requirement_scores = [[-1 for i in range(len(requirements))] for j in range(len(blocks))]

        print(requirement_scores) if self.debug else None

        for block_index, block in enumerate(blocks):
            print(f'index: {block_index} block values: {block}') if self.debug else None
            for requirement_index, requirement in enumerate(requirements):
                for comparative_index in range(len(blocks)):
                    print(f'comparative_index: {comparative_index} block_index: {block_index}') if self.debug else None
                    value_index = abs(block_index - comparative_index)
                    starting_values = blocks[block_index]
                    comparative_values = blocks[comparative_index]
                    print(f'{requirement}:{starting_values} vs {comparative_values} -> {value_index}') if self.debug else None
                    if comparative_values[requirement] is True:
                        print(f'Sevice: {requirement} FOUND in block: {comparative_index}') if self.debug else None
                        if requirement_scores[block_index][requirement_index] == -1:
                            requirement_scores[block_index][requirement_index] = value_index
                            print(f'{requirement_scores} {block_index} {requirement_index}') if self.debug else None
                            if requirement_scores[block_index][requirement_index] == 0:
                                break
                        elif requirement_scores[block_index][requirement_index] > value_index:
                            requirement_scores[block_index][requirement_index] = value_index
                            print(f'{requirement_scores} {block_index} {requirement_index}') if self.debug else None
                            break
                    else:
                        print(f'Sevice: {requirement} NOT FOUND in block: {comparative_index}') if self.debug else None

        print(requirement_scores) if self.debug else None

        return self.calculate_best_fit(requirement_scores)

    def calculate_best_fit(self, requirement_scores: List[List[int]]) -> int:
        scores = [0 for index in range(len(requirement_scores))]
        minimum_score = 99999999
        minimum_index = 99999999
        for idx, block_score in enumerate(requirement_scores):
            score = 0
            for value in block_score:
                score += value
            scores[idx] = score
            if score < minimum_score:
                minimum_score = score
                minimum_index = idx

        return minimum_index


def main():
    blocks = [
        {"gym": False, "school": True, "store": False},
        {"gym": True, "school": False, "store": False},
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True}
    ]

    requirements = ["gym", "school", "store"]

    basic_needs = BasicNeeds(True)
    print(basic_needs.assess_blocks(blocks, requirements))


if __name__ == '__main__':
    main()
