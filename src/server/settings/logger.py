import logging
import sys
import time
import traceback

from flask import request


def create_logger():  # pytest에서는 로그를 저장 안함
    if not sys.argv[0].endswith('test'):  # use not on pytest
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(levelname)s : %(message)s')  # 로그 앞에 로그 레벨을 표시

        file_handler = logging.FileHandler('LOG.log')  # 파일로 로그 저장
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()  # 콘솔에 로그 표시
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        flask_log = logging.getLogger('werkzeug')  # 기본 앱서버 로그 끔
        flask_log.disabled = True

        gevent_log = logging.getLogger('gevent')  # gevent 로그 끔
        gevent_log.disabled = True
    else:
        logger = logging.getLogger(__name__)
    return logger


logger = create_logger()


def after_request(response):  # 정상적으로 처리시 로그를 남김
    if not request.url.endswith('/favicon.ico'):  # favicon 무시
        logger.info(f'{request.remote_addr} {time.strftime("%Y-%m-%d  %X", time.localtime(time.time()))}  '
                    f'{request.method} {request.url} {response.status_code} - {request.user_agent}')
    return response


def trace_back_recent_call():  # 오류가 난 코드의 위치를 스트링으로 반환함.
    error_location = traceback.format_exc()
    return error_location


def error_handler(error):  # 에러 발생시 로그를 남김
    logger.error(f'{request.remote_addr} {time.strftime("%Y-%m-%d  %X", time.localtime(time.time()))} '
                 f'{request.method} {request.url} {error.code} - {request.user_agent} \n {trace_back_recent_call()}')
