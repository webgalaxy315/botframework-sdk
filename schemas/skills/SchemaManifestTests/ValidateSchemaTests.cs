// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Schema;
using NJsonSchema;
using NJsonSchema.Generation;
using Xunit;
using JsonSchema = NJsonSchema.JsonSchema;
using JsonSchemaResolver = NJsonSchema.Generation.JsonSchemaResolver;

namespace SchemaManifestTests
{
    /// <summary>
    /// Validates sample manifests against schemas.
    /// </summary>
    /// <remarks>
    /// There are some differences on the validation provided by Newtonsoft and NJsonSchema so we use both libraries in the tests
    /// to ensure better compatibility.
    /// </remarks>
    public class ValidateSchemaTests
    {
        // List of schema version folders to test.
        private static readonly List<string> _schemaVersionFolders = new List<string>
        {
            "v2.0",
            "v2.1",
            "v2.2"
        };

        // Path to the folder containing the schema files and samples (relative to where the test is executing).
        private static readonly string _schemasRootFolder = Path.Combine(Directory.GetCurrentDirectory(), "../../../../");

        /// <summary>
        /// Builds the list of manifest schemas and samples to validate from the file system.
        /// </summary>
        public static TheoryData<string, string> GetManifestAndSamples()
        {
            var manifestAndSamples = new TheoryData<string, string>();

            foreach (var schemaVersion in _schemaVersionFolders)
            {
                var schemaFolder = Path.Combine(_schemasRootFolder, schemaVersion);
                var samplesFolder = Path.Combine(schemaFolder, "Samples");
                var sampleManifestFiles = Directory.GetFileSystemEntries(samplesFolder, "*.json", SearchOption.AllDirectories);
                foreach (var manifestFile in sampleManifestFiles)
                {
                    var manifestRelativePath = Path.GetRelativePath(schemaFolder, manifestFile);
                    manifestAndSamples.Add(schemaVersion, manifestRelativePath);
                }
            }

            return manifestAndSamples;
        }

        [Theory]
        [MemberData(nameof(GetManifestAndSamples))]
        public async Task ValidateManifestSamplesAgainstSchemasUsingNJsonSchemaAsync(string schemaVersion, string sampleManifest)
        {
            // Arrange
            var manifestSchemaPath = Path.Combine(_schemasRootFolder, schemaVersion, "skill-manifest.json");
            var manifestSchema = await GetSchemaAsync(manifestSchemaPath);

            var sampleManifestPath = Path.Combine(_schemasRootFolder, schemaVersion, sampleManifest);
            var sampleManifestText = await File.ReadAllTextAsync(sampleManifestPath);

            // Act
            var validationErrors = manifestSchema.Validate(sampleManifestText);

            // Assert
            Assert.Empty(validationErrors);
        }

        [Theory]
        [MemberData(nameof(GetManifestAndSamples))]
        public async Task ValidateManifestSamplesAgainstSchemasUsingNewtonsoftSchemaAsync(string schemaVersion, string sampleManifest)
        {
            // Note: you can use https://www.jsonschemavalidator.net/ for an interactive version.

            // Arrange
            var manifestSchemaPath = Path.Combine(_schemasRootFolder, schemaVersion, "skill-manifest.json");
            var manifestSchema = JSchema.Parse(await File.ReadAllTextAsync(manifestSchemaPath), new JSchemaUrlResolver());

            var sampleManifestPath = Path.Combine(_schemasRootFolder, schemaVersion, sampleManifest);
            var json = JToken.Parse(await File.ReadAllTextAsync(sampleManifestPath));

            // Act
            json.IsValid(manifestSchema, out IList<ValidationError> validationErrors);

            // Assert
            Assert.Empty(validationErrors);
        }

        private static async Task<JsonSchema> GetSchemaAsync(string schemaPath)
        {
            var rawSchemaText = await File.ReadAllTextAsync(schemaPath);

            return await JsonSchema.FromJsonAsync(rawSchemaText, null, x =>
            {
                var schemaResolver = new JsonSchemaResolver(x, new JsonSchemaGeneratorSettings());
                var referenceResolver = new JsonReferenceResolver(schemaResolver);
                referenceResolver.AddDocumentReference("http://json-schema.org/draft-07/schema", JsonSchema.CreateAnySchema());

                return referenceResolver;
            });
        }
    }
}
