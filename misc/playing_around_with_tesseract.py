import cv2
# import os, argparse
# import pytesseract
# from PIL import Image

class ImageRecognition:
    def __init__(self, filename: str = None):
        self.filename = filename

    def scan_image_for_text(self, text: str) -> str:
        images = cv2.imread(self.filename)
        return ""
