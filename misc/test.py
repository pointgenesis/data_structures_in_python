class Test:

    def __init__(self, blocks, requirements):
        self.blocks = blocks
        self.requirements = requirements

    def find_best_fit(self):
        hassle_scores = {}
        for block_idx, block in enumerate(blocks):
            for requirement_idx, requirement in enumerate(requirements):
                if block[requirement]:
                    print(f'requirement: {requirement} was found at index: {block_idx}')
                    hassle_score = block_idx *


if __name__ == '__main__':
    blocks = [
        {
            "store": False,
            "gym": True,
            "school": False
        },
        {
            "store": False,
            "gym": False,
            "school": False
        },
        {
            "store": True,
            "gym": True,
            "school": False
        },
        {
            "store": False,
            "gym": True,
            "school": False
        },
        {
            "store": False,
            "gym": False,
            "school": True
        },
    ]
    requirements = ["gym", "store"]
    test = Test(blocks, requirements)
    test.find_best_fit()
