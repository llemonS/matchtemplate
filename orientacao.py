import argparse
import cv2
''' 
     uso:
     orientacao.py --imagem nomedaimagem.jpg
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagem", required=True,
	help="diretorio_da_imagem")
args = vars(ap.parse_args())
image = cv2.imread(args["imagem"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
	angle = -(90 + angle)
else:
	angle = -angle
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
print("angulo: {:.3f}".format(angle))
cv2.imwrite(str("imagem_editada_"+args["imagem"]), rotated)