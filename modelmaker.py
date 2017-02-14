# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:01:14 2017

@author: Koji
"""

import numpy as np
import scipy.spatial #Delaunay

def writeToPLY(filename, vertices, faces):
    """
    PLYファイルにモデル情報を書き込む

    Parameters
    -----
    filename (string)
        書き込み先のファイル名
    
    vertices (ndarray)   
        頂点の座標情報が保持されているN*3の行列
    
    faces (ndarray)
        面を構成する3つの頂点のインデックスが，複数列挙されたN*3の行列    
    
    Returns
    -----
    None
    
    """
    
    file = open(filename, "w")
  
    #ヘッダの書き込み
    header_txt = "ply\nformat ascii 1.0\ncomment ShadowMaker\nelement vertex "+str(len(vertices))+"\n"
    header_txt += "property float x\nproperty float y\nproperty float z\nelement face "+str(len(faces))+"\n"
    header_txt += "property list uchar int vertex_index\nend_header\n"    
    file.write(header_txt)    
    
    for vertex in vertices:
        vertex_txt = str(vertex[0])+ " "+ str(vertex[1])+ " "+str(vertex[2])+ "\n"  
        file.write(vertex_txt)
   
    for face in faces:
        face_txt = "3 "+str(face[0])+ " "+ str(face[1])+ " "+str(face[2])+ "\n" 
        file.write(face_txt)         
     
    file.close()
    return    
    
def createModel(img):
    """
    画像から3次元モデルを生成する

    Parameters
    -----
    img (ndarray)
        対象の画像
    
    Returns
    -----
    None
    
    """
    
    #頂点の生成
    num_vertices = img.shape[0] * img.shape[1]
    vertices = np.empty((num_vertices, 2))
    for i in np.arange(0,num_vertices):
        row_index = i/img.shape[1]
        col_index = i%img.shape[1]
        vertices[i,0] = row_index
        vertices[i,1] = col_index
    
    #ドロネー三角形分割によるメッシュ生成
    delaunay = scipy.spatial.Delaunay(vertices) 
    faces = delaunay.vertices
    
    #depth決定
    vertices = np.hstack(( vertices, np.empty((len(vertices),1)) )) #depth用に次元を拡張
    
    for (i,v) in enumerate(vertices):
        row_index = i/img.shape[1]
        col_index = i%img.shape[1]       
        v[2] = img[row_index, col_index]
    
    #ファイル書き込み    
    writeToPLY("aaa.ply", vertices, faces)
    
    return