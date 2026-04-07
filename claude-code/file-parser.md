> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 文件解析(同步)

> 创建文件解析任务，支持多种文件格式和解析工具。见 [文件解析服务](/cn/guide/tools/file-parser)



## OpenAPI

````yaml /openapi/openapi.json post /paas/v4/files/parser/sync
openapi: 3.0.1
info:
  title: ZHIPU AI API
  description: ZHIPU AI 接口提供强大的 AI 能力，包括聊天对话、工具调用和视频生成。
  license:
    name: ZHIPU AI 开发者协议和政策
    url: https://chat.z.ai/legal-agreement/terms-of-service
  version: 1.0.0
  contact:
    name: Z.AI 开发者
    url: https://chat.z.ai/legal-agreement/privacy-policy
    email: user_feedback@z.ai
servers:
  - url: https://open.bigmodel.cn/api/
    description: 开放平台服务
security:
  - bearerAuth: []
tags:
  - name: 模型 API
    description: Chat API
  - name: 工具 API
    description: Web Search API
  - name: Agent API
    description: Agent API
  - name: 文件 API
    description: File API
  - name: 知识库 API
    description: Knowledge API
  - name: 实时 API
    description: Realtime API
  - name: 批处理 API
    description: Batch API
  - name: 助理 API
    description: Assistant API
  - name: 智能体 API（旧）
    description: QingLiu Agent API
paths:
  /paas/v4/files/parser/sync:
    post:
      tags:
        - 工具 API
      summary: 文件解析(同步)
      description: 创建文件解析任务，支持多种文件格式和解析工具。见 [文件解析服务](/cn/guide/tools/file-parser)
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                  description: 待解析文件
                tool_type:
                  type: string
                  enum:
                    - prime-sync
                  description: 使用的解析工具类型
                file_type:
                  type: string
                  enum:
                    - WPS
                    - PDF
                    - DOCX
                    - DOC
                    - XLS
                    - XLSX
                    - PPT
                    - PPTX
                    - PNG
                    - JPG
                    - JPEG
                    - CSV
                    - TXT
                    - MD
                    - HTML
                    - BMP
                    - GIF
                    - WEBP
                    - HEIC
                    - EPS
                    - ICNS
                    - IM
                    - PCX
                    - PPM
                    - TIFF
                    - XBM
                    - HEIF
                    - JP2
                  description: >-
                    文件类型支持：pdf,docx,doc,xls,xlsx,ppt,pptx,png,jpg,jpeg,csv,txt,md,html,bmp,gif,webp,heic,eps,icns,im,pcx,ppm,tiff,xbm,heif,jp2
              required:
                - file
                - tool_type
        required: true
      responses:
        '200':
          description: 结果获取成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileParseResultResponse'
        default:
          description: 请求失败。
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    FileParseResultResponse:
      type: object
      properties:
        status:
          type: string
          enum:
            - processing
            - succeeded
            - failed
          description: 任务处理状态
          example: succeeded
        message:
          type: string
          description: 结果状态描述
          example: 结果获取成功
        content:
          type: string
          description: 当`format_type=text`时返回的解析文本内容
          example: 这是解析后的文本内容...
          nullable: true
        task_id:
          type: string
          description: 文件解析任务`ID`
          example: task_123456789
        parsing_result_url:
          type: string
          description: 当`format_type=download_link`时返回的结果下载链接
          example: https://example.com/download/result.zip
          nullable: true
      required:
        - status
        - message
        - task_id
    Error:
      type: object
      properties:
        error:
          required:
            - code
            - message
          type: object
          properties:
            code:
              type: string
            message:
              type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        使用以下格式进行身份验证：Bearer [<your api
        key>](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

````

Built with [Mintlify](https://mintlify.com).
