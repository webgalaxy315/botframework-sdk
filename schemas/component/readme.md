# Component Schema
The component schema defines extensions to JsonSchema for supporting
Bot Framework declarative component definitions (via .schema files which describe the shape of .dialog files).

The extensions are in baseComponent.schema and bf dialog:merge -u will 
merge baseComponent.schema + json.schema => component.schema

## Published location

The component JSON schemas are published at:

`https://schemas.botframework.com/schemas/component/v{version}/component.schema`

Example:

`https://schemas.botframework.com/schemas/component/v1.0/component.schema`

You should use the published version when referencing this schema.

## Legacy versions

The `component.schema` and `definitions.schema` files are left in the root folder for backwards compatibility purposes, and should not be used. Use the `\v{version}\component.schema` version instead.
