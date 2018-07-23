# coding=utf-8
import logging

logging.basicConfig(filename='../LOG/' + __name__ + '.log',
                    format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
                    filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')