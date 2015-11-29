# coding:utf-8
import numpy
import math
from matplotlib import pyplot

def make_rotate_matrix(rad):
	'''回転行列の生成'''
	return numpy.array([[math.cos(rad),-math.sin(rad)],
			    [math.sin(rad),math.cos(rad)]]).transpose()

def main():
	num = 20
	#計算結果の保持用
	x_positions = []
	y_positions = []

	#(1,0)という向きのベクトル
	base = numpy.array([1,0])

	print('degree \t result')

	for x in range(num+1):

	  #回転させる角度をラジアンで計算
	  rad = x * math.pi * 2 / num
	  #回転行列を生成
	  rot = make_rotate_matrix(rad)
	  #表示用に度を計算
	  deg = 360 / num * x
	  #numpy.dotを使用して回転させる
	  result = numpy.dot(base,rot)
	  #結果の出力
  	  print(deg, '\t' ,result)

	  #保存
	  x_positions.append(result[0])
	  y_positions.append(result[1])

	#プロット
	pyplot.plot(x_positions, y_positions)
	#y軸のラベル
	pyplot.ylabel('Y-axis')
	#x軸のラベル
	pyplot.xlabel('X-axis')
	#UI&描画
	pyplot.show()
	  
if __name__ == '__main__':
 main();
