import subprocess
import urllib2
import requests
import json
class Response:
    frame=None
    ipsrc=None
    ipdest=None
    requestversion = None
    response_code=None
    response_phrase=None
    date=None
    server=None
    last_modified=None
    content_length=None
    connection=None
    content_type=None
    def __init__(self,frame,file):
        self.frame=frame
        # khoi tao ipsrc,dest
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e ip.src -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.ipsrc = p
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e ip.dst -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.ipdest = p
        # khoi tao requestversion
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.request.version -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.requestversion = p
        # khoi tao response code
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.response.code -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.response_code = p
        # khoi tao response phrase
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.response.phrase -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.response_phrase = p
        # khoi tao response phrase
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.date -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.date = p
        # khoi tao server
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.server -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.server = p
        # khoi tao last modified
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.last_modified -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.last_modified = p
        # khoi tao content length
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.content_length -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.content_length = p
        # khoi tao connection
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.connection -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.connection= p
        # khoi tao content type
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.content_type -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.content_type=p

    def frame(self):
        return self.frame

    def ipsrc(self):
        return self.ipsrc

    def ipdest(self):
        return self.ipdest

    def requestversion(self):
        return self.requestversion

    def response_code(self):
        return self.response_code

    def response_phrase(self):
        return self.response_phrase

    def date(self):
        return self.date

    def server(self):
        return self.server

    def last_modified(self):
        return self.last_modified

    def content_length(self):
        return self.content_length

    def connection(self):
        return self.connection

    def content_type(self):
        return self.content_type








class Request:
    frame=None
    ipsrc=None
    ipdest=None
    host=None
    method=None
    uri=None
    requestversion=None
    user_agent=None
    browser=None
    accept = None
    accept_language = None
    accept_encoding = None
    connection = None
    operating_system=None
    browser_version_full=None
    if_modified_since=None
    def __init__(self,frame,file):
        self.frame=frame
        #khoi tao ipsrc,dest
        s = 'frame.number=='+  frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e ip.src -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p=p.replace("\n","")
        self.ipsrc=p
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e ip.dst -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.ipdest = p
        # khoi tao host
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.host -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.host = p
        # khoi tao method
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.request.method -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.method = p
        # khoi tao uri
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.request.uri -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.uri = p
        # khoi tao requestversion
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.request.version -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.requestversion = p
        # khoi tao useragent
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.request.version -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.user_agent = p
        #khoi tao browser,operating,browser version full  system su dung whatismybrowser.com API

        # the url of the API
        url = "https://api.whatismybrowser.com/api/v1/user_agent_parse"

        # put your api key in this variable:
        user_key = "2e3c449f1e5a094a637517494b5893ae"

        # the user agent to parse
        user_agent = self.user_agent

        # -- prepare data for the API request
        post_data = {
            'user_key': user_key,
            'user_agent': user_agent,
        }

        # -- make the request to the whatismybrowser server
        result = requests.post(url, data=post_data)

        # -- check that the server responded with a "200/Success" code
        if result.status_code != 200:
            print result.text

        # -- try to decode the api response as json
        try:
            result_json = result.json()
        except Exception, e:
            print "Couldn't decode the response as JSON:", e

        # -- check the API request was successful
        if result_json.get('result') != "success":
            raise Exception(
                "The API did not return a 'success' response. It said: result: %s, message_code: %s, message: %s" % (
                result_json.get('result'), result_json.get('message_code'), result_json.get('message')))

        # now you have "result_json" and can store, display or process any part of the response.
        # for example:
        # print result_json.get('parse').get('simple_browser_string')

        # Please refer to the documentation on https://developers.whatismybrowser.com for a
        # full list of the available fields and their intended usage.

        # -- print the entire json dump for reference
        # print json.dumps(result_json, indent=2)
        self.browser=result_json["parse"]["browser"]
        self.operating_system=result_json["parse"]["operating_system"]
        self.browser_version_full=result_json["parse"]["browser_version_full"]
        # # khoi tao accept
        # s = 'frame.number==' + frame
        # s1 = "\"" + s + "\""
        # cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.accept -T fields'
        # p = subprocess.check_output(cmdstring, shell=True)
        # p = p.replace("\n", "")
        # self.accept = p

        # khoi tao accept language
        s = 'frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.accept_language -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        p = p.replace("\n", "")
        self.accept_language = p

        # # khoi tao accept encoding
        # s = 'frame.number==' + frame
        # s1 = "\"" + s + "\""
        # cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.accept_encoding -T fields'
        # p = subprocess.check_output(cmdstring, shell=True)
        # p = p.replace("\n", "")
        # self.accept_encoding = p
        #
        # # khoi tao connection
        # s = 'frame.number==' + frame
        # s1 = "\"" + s + "\""
        # cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.connection -T fields'
        # p = subprocess.check_output(cmdstring, shell=True)
        # p = p.replace("\n", "")
        # self.connection = p



        # khoi tao if_modified_since
        s = 'http.request.line contains If-Modified-Since and frame.number==' + frame
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e frame.number -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        if(p==""):
            self.if_modified_since=False
        else:
            self.if_modified_since=True

    def frame(self):
        return self.frame

    def ipsrc(self):
        return self.ipsrc

    def ipdest(self):
        return self.ipdest

    def method(self):
        return self.method

    def uri(self):
        return self.uri

    def requestversion(self):
        return self.requestversion

    def user_agent(self):
        return self.user_agent

    def browser(self):
        return self.browser

    def accept(self):
        return self.accept

    def accept_language(self):
        return self.accept_language

    def accept_encoding(self):
        return self.accept_encoding

    def connection(self):
        return self.connection

    def operating_system(self):
        return self.operating_system

    def browser_version_full(self):
        return self.browser_version_full

    def contain_if_modified_since(self):
        return self.if_modified_since


class Http:
    host=[]             #All host of request
    browser=[]
    frame=[]            #frame all http
    framerequest=[]     #frame all http request
    frameresponse=[]    #frame all http response
    requestarray=[]          #All request object
    responsearray=[]         #All response object
    file=None
    def __init__(self,file):
        self.file=file
        s = 'http'  # +' and not http contains favicon.ico'
        s1 = "\"" + s + "\""
        cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e frame.number -T fields'
        p = subprocess.check_output(cmdstring, shell=True)
        # frame string to array
        position1 = -1
        position2 = p.find('\n')
        frame = []
        # Tim ra cac frame number la GET
        while (position2 != -1):
            temp = p[position1 + 1:position2]
            frame.append(temp)
            position1 = position2
            position2 = p.find('\n', position1 + 1)
        self.frame = frame
        s = 'frame.number=='
        # Duyet tat ca frame, khoi tao frame request,response
        for i in range(len(frame)):
            # Lay ra http.request.method : Neu co thi la request, khong co la response

            s1 = "\"" + s + frame[i]+ "\""
            cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.request.method -T fields'
            p = subprocess.check_output(cmdstring, shell=True)
            if (p != "\n"):
                self.framerequest.append(frame[i])
            else:
                self.frameresponse.append(frame[i])

        s = 'frame.number=='

        #Duyet tat ca framerequest, lay ra host, khoi tao Request object
        for i in range(len(self.framerequest)):
            s1 = "\"" + s+ self.framerequest[i] + "\""
            cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e http.host -T fields'
            p = subprocess.check_output(cmdstring, shell=True)
            p=p.replace("\n","")
            self.host.append(p)
            #Khoi tao Request object
            request=Request((self.framerequest)[i],file)
            (self.requestarray).append(request)

        #Duyet tat ca frame response, khoi tao Response object
        for i in range(len(self.frameresponse)):
            #Khoi tao Response object
            response=Response(self.frameresponse[i],file)
            self.responsearray.append(response)


    def requestarr(self):
        return self.requestarray




    def returnhost(self):
        return self.host


#
#
#
#
#
#
#
#
# # return lai object http_version
# def http_version(host, file):
#     # ---------------client------------------
#     # Lay ra tat ca cac version cua http request toi host
#     s = 'http and http.host==' + host #+ ' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.request.version -T fields"
#     p = subprocess.check_output(cmdstring, shell=True)
#     # p = subprocess.check_output(
#     #     'tshark -r /home/mitom/Desktop/taothu/http1.pcap -Y "http contains gaia.cs.umass.edu" -e http.request.version -T fields',
#     #     shell=True)
#     # Cac version nay chia cach boi \n -> Chia ra roi cho vao array
#     position1 = -1
#     position2 = p.find('\n')
#     version = []  # array version
#     while (position2 != -1):
#         temp = p[position1+1:position2]
#         version.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     # Cho cac version nay vao Array client neu no DISTINCT
#     arrayclient = []
#     arrayclient.append(version[0])
#     for i in range(len(version)):
#         for j in range(len(arrayclient)):
#             if (version[i] != arrayclient[j]):
#                 arrayclient.append(version[i])
#     # ---------------host------------------
#     # Lay ra tat ca cac version cua http request toi host
#     ipaddress = ip_address(host,file)
#     ip_host = ipaddress["host"]
#     s = 'http and ip.src==' + ip_host #+ ' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.request.version -T fields"
#     p = subprocess.check_output(cmdstring, shell=True)
#     # Cac version nay chia cach boi Space -> Chia ra roi cho vao array
#     position1 = -1
#     position2 = p.find('\n')
#     version = []  # array version
#     while (position2 != -1):
#         temp = p[position1+1:position2]
#         version.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     # Cho cac version nay vao Array host neu no DISTINCT
#     arrayhost = []
#     arrayhost.append(version[0])
#     for i in range(len(version)):
#         for j in range(len(arrayhost)):
#             if (version[i] != arrayhost[j]):
#                 arrayhost.append(version[i])
#
#     # Cho 2 array vao httpversion va return
#     httpversion = dict()
#     httpversion["client"] = arrayclient
#     httpversion["host"] = arrayhost
#     return httpversion
#
#
# def status_code_with_frame_number(framenumber,file):
#     s = "frame.number=="+framenumber
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.response.code -T fields"
#     p = subprocess.check_output(cmdstring, shell=True)
#     return p
#
# def response_phrase_with_frame_number(framenumber,file):
#     s = "frame.number==" + framenumber
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.response.phrase -T fields"
#     p = subprocess.check_output(cmdstring, shell=True)
#     return p
#
# # chua co TH 1 may' 2 IP khac nhau
# def ip_address(host, file):
#     s = 'http and http.host==' + host #+ ' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e ip.src -T fields"
#     # Source ip
#     p_src = subprocess.check_output(cmdstring, shell=True)
#     # Get substring from p
#     p_src1 = p_src.find('\n')
#     p_src2 = p_src[:p_src1]
#     # Dest Ip
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e ip.dst -T fields"
#     p_dest = subprocess.check_output(cmdstring, shell=True)
#     p_dest1 = p_dest.find('\n')
#     p_dest2 = p_dest[:p_dest1]
#     # Dictionary contain client,host
#     ipaddress = dict()
#     ipaddress["client"] = p_src2
#     ipaddress["host"] = p_dest2
#     return ipaddress
#
#
# def accept_language(host, file):
#     # lay ra cac accept language cua browser khi request toi host
#     s = 'http and http.host==' + host #+ ' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.accept_language -T fields"
#     p = subprocess.check_output(cmdstring, shell=True)
#
#     # Cac version nay chia cach boi Space -> Chia ra roi cho vao array
#     position1 = -1
#     position2 = p.find('\n')
#     accept = []  # array version
#     while (position2 != -1):
#         temp = p[position1+1:position2]
#         accept.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     # Cho cac version nay vao Array host neu no DISTINCT
#     arrayclient = []
#     arrayclient.append(accept[0])
#     for i in range(len(accept)):
#         for j in range(len(arrayclient)):
#             if (arrayclient[j] != accept[i]):
#                 arrayclient.append(accept[i])
#     #
#     acceptlanguage = dict()
#     acceptlanguage["accept_language"] = arrayclient
#     return acceptlanguage
#
#
# def status_code(host, file):
#     # Lay ra tat ca cac status code cua host ve client
#     ipaddress = ip_address(host,file)
#     ip_host = ipaddress["host"]
#     s = 'http and ip.src==' + ip_host #+ ' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.response.code -T fields"
#
#     p = subprocess.check_output(
#         cmdstring,
#         shell=True)
#     # Cac status nay chia cach boi \n -> Chia ra roi cho vao array
#     position1 = -1
#     position2 = p.find('\n')
#     response = []  # array version
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         response.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     # Tra ve 1 dictionary status code tu host
#     statuscode = dict()
#     statuscode["response_code"] = response
#     return statuscode
#
# def response_phrase(host, file):
#     # Lay ra tat ca cac status phrase cua host ve client
#     ipaddress = ip_address(host,file)
#     ip_host = ipaddress["host"]
#     s = 'http and ip.src==' + ip_host #+ ' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.response.phrase -T fields"
#
#     p = subprocess.check_output(
#         cmdstring,
#         shell=True)
#     # Cac status nay chia cach boi \n -> Chia ra roi cho vao array
#     position1 = -1
#     position2 = p.find('\n')
#     response = []  # array version
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         response.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     # Tra ve 1 dictionary status code tu host
#     responsephrase = dict()
#     responsephrase["response_phrase"] = response
#     return responsephrase
#
#
#
#
# def last_modified(host, file):
#     # Lay ra tat ca cac last modified cua host ve client
#     ipaddress = ip_address(host,file)
#     ip_host = ipaddress["host"]
#     s = 'http and ip.src==' + ip_host #+ ' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.last_modified -T fields"
#
#     p = subprocess.check_output(
#         cmdstring,
#         shell=True)
#     # Cac last modified nay chia cach boi \n -> Chia ra roi cho vao array
#     position1 = -1
#     position2 = p.find('\n')
#     lastmdf = []  # array last modified
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         lastmdf.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     lastmodified = dict()
#     lastmodified["last_modified"] = lastmdf
#     return lastmodified
#
#
# def content_length(host, file):
#     # Lay ra tat ca cac content length cua host ve client
#     ipaddress = ip_address(host,file)
#     ip_host = ipaddress["host"]
#     s = 'http and ip.src==' + ip_host #+ ' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + " -e http.content_length -T fields"
#
#     p = subprocess.check_output(
#         cmdstring,
#         shell=True)
#
#     # Cac content length nay chia cach boi \n -> Chia ra roi cho vao array
#     position1 = -1
#     position2 = p.find('\n')
#     contentl = []  # array last modified
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         contentl.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     contentlength = dict()
#     contentlength["content_length"] = contentl
#     return contentlength
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def frame_contain_if_modified_since( file):
#     s = 'http' +' and http.request.line contains If-Modified-Since'#+" and not http contains favicon.ico"
#     s1 = "\"" + s + "\""
#     cmdstring='tshark -r '+file+' -Y '+s1+' -e frame.number -T fields'
#     p = subprocess.check_output(cmdstring, shell=True)
#     # frame string to array
#     position1 = -1
#     position2 = p.find('\n')
#     frame = []
#     # Tim ra cac frame number la GET
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         frame.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     return frame
#
# def frame_get(host, file):
#     # get GET's frame number to host
#     s = 'http and http.host==' + host+' and http.request.method=='+"\""+"GET"+"\""#+" and not http contains favicon.ico"
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + ' -e frame.number -T fields'
#     p = subprocess.check_output(cmdstring, shell=True)
#     # frame string to array
#     position1 = -1
#     position2 = p.find('\n')
#     frame = []
#     # Tim ra cac frame number la GET
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         frame.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     return frame
#
# def frame_get_no_host(file):
#     s = 'http'+ ' and http.request.method==' + "\"" + "GET" + "\""  # +" and not http contains favicon.ico"
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e frame.number -T fields'
#     p = subprocess.check_output(cmdstring, shell=True)
#     # frame string to array
#     position1 = -1
#     position2 = p.find('\n')
#     frame = []
#     # Tim ra cac frame number la GET
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         frame.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     return frame
#
# def frame_request(host, file):
#     # get GET's frame number to host
#     s = 'http and http.host==' + host#+' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + ' -e frame.number -T fields'
#     p = subprocess.check_output(cmdstring, shell=True)
#     # frame string to array
#     position1 = -1
#     position2 = p.find('\n')
#     frame = []
#     # Tim ra cac frame number la GET
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         frame.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     return frame
#
#
# def frame_response(host, file):
#     # get RESPONSE's frame number to host
#     ipaddress = ip_address(host,file)
#     ip_host = ipaddress["host"]
#     s = 'http and ip.src==' + ip_host #+' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r '+file+' -Y ' + s1 + ' -e frame.number -T fields'
#     # frame string to array
#     p = subprocess.check_output(cmdstring, shell=True)
#     position1 = -1
#     position2 = p.find('\n')
#     frame = []
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         frame.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     return frame
#
#
#
#
# def frame_requese_no_host(file):
#     # get GET's frame number to host
#     s = 'http'# +' and not http contains favicon.ico'
#     s1 = "\"" + s + "\""
#     cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e frame.number -T fields'
#     p = subprocess.check_output(cmdstring, shell=True)
#     # frame string to array
#     position1 = -1
#     position2 = p.find('\n')
#     frame = []
#     # Tim ra cac frame number la GET
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         frame.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     return frame
#
# def frame_number_contains_some_string(file,string):
#     s = 'http' +' and http contains '+"\""+string+"\""  # +" and not http contains favicon.ico"
#     s1 = "\'" + s + "\'"
#     cmdstring = 'tshark -r ' + file + ' -Y ' + s1 + ' -e frame.number -T fields'
#     p = subprocess.check_output(cmdstring, shell=True)
#     # frame string to array
#     p = subprocess.check_output(cmdstring, shell=True)
#     position1 = -1
#     position2 = p.find('\n')
#     frame = []
#     while (position2 != -1):
#         temp = p[position1 + 1:position2]
#         frame.append(temp)
#         position1 = position2
#         position2 = p.find('\n', position1 + 1)
#     return frame


    # {
    # "q1":{
    #   "http_version":{
    #       "client":[1.1,1.0]
    #       "host":[]
    #    }
    # }
    # "q2":{
    #   "ip_address":{
    #       "client":""
    #       "host":""
    #   }
    #
    # }
    # accept_language:{
    #   "client":[]
    # }
    #   status_code:{
    #       "host":[]
    # }
    #  last_modified:{
    #       "host":[]
    #   }
    #
    #
    #
    #
    #

# }

###

# Bam 1 nut tao pcap
# bam 1 nut tao cau tra loi voi dau vao la host. Hay la service gui TRA loi ve host.
#question 12 caan xem sao de x/d GET message . Phan biet voi chi contains string
