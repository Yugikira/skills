# IMA 知识库文件移动 API 详解

## 接口端点

`/openapi/wiki/v1/move_knowledge`

**触发场景**：用户需要将文件从一个知识库移动到另一个知识库，支持批量文件移动操作。

**请求体结构**
```json
{
  "src_knowledge_base_id": "string, 必填, 源知识库 ID",
  "dst_knowledge_base_id": "string, 必填, 目标知识库 ID",
  "dst_folder_id": "string, 可选, 目标文件夹 ID（不传则移到目标知识库根目录）",
  "src_knowledge_base_name": "string, 可选, 源知识库名称，用于二次校验",
  "dst_knowledge_base_name": "string, 可选, 目标知识库名称，用于二次校验",
  "dst_folder_name": "string, 可选, 目标文件夹名称，用于二次校验",
  "infos": [
    { "media_id": "string, 必填, 要移动的文件/文件夹 ID" }
  ]
}
```

**返回体结构**
```json
{
  "move_results": {
    "media_id": {
      "ret_code": "int32, 返回码",
      "err_msg": "string, 错误信息"
    }
  }
}
```

**curl 调用示例**
```bash
curl -s -X POST "https://ima.qq.com/openapi/wiki/v1/move_knowledge" \
    -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
    -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
    -H "Content-Type: application/json" \
    -d '{
      "src_knowledge_base_id": "源知识库ID",
      "dst_knowledge_base_id": "目标知识库ID",
      "dst_folder_id": "目标文件夹ID（可省略）",
      "infos": [
        { "media_id": "文件ID1" },
        { "media_id": "文件ID2" }
      ]
    }'
```

## 要点速查
|项目|	说明|
|:--|:--|
|批量移动|	`infos` 数组最多放 10 个 `media_id`|
|跨知识库|	源和目标可以是不同知识库|
|目标文件夹|	`dst_folder_id` 不传则移到根目录|
|名称校验|	传 `*_name` 字段会额外做名称匹配验证，防止传错 ID|
|获取 media_id|	通过 `get_knowledge_list` 或 `search_knowledge` 接口获取|
|获取 kb_id|	通过 `search_knowledge_base` 接口获取|
|认证方式|	`Header` 中传 `ima-openapi-clientid` 和 `ima-openapi-apikey`，环境变量自动注入|

## Skill 中的典型调用流程
1. 查源库 → `search_knowledge_base` 获取 `src_knowledge_base_id`
2. 获取文件 ID → `get_knowledge_list` 或 `search_knowledge` 获取 `media_id`
3. 查目标库 → `search_knowledge_base` 获取 `dst_knowledge_base_id`
4. 执行移动 → `move_knowledge` 完成文件迁移
