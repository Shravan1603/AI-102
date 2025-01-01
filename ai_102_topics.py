# ai_102_topics.py

ai_102_topics = {
    "Plan and Manage an Azure AI Solution": [
        ("Select the appropriate Azure AI service", 10, [
            ("Select the appropriate service for computer vision", 5),
            ("Select the appropriate service for NLP", 5),
            ("Select the appropriate service for speech", 5),
            ("Select the appropriate service for generative AI", 5),
            ("Select the appropriate service for document intelligence", 5),
            ("Select the appropriate service for knowledge mining", 5),
        ]),
        ("Plan, create, and deploy an Azure AI service", 20, [
            ("Plan for Responsible AI principles", 5),
            ("Create an Azure AI resource", 5),
            ("Determine a default endpoint for a service", 5),
            ("Integrate Azure AI services into CI/CD", 5),
        ]),
        ("Manage, monitor, and secure an Azure AI service", 20, [
            ("Configure diagnostic logging", 5),
            ("Monitor an Azure AI resource", 5),
            ("Manage costs for Azure AI services", 5),
            ("Manage account keys", 5),
        ]),
    ],
    "Implement Content Moderation Solutions": [
        ("Create solutions for content delivery", 10, [
            ("Implement text moderation with Azure AI Content Safety", 5),
            ("Implement image moderation with Azure AI Content Safety", 5),
        ]),
    ],
    "Implement Computer Vision Solutions": [
        ("Analyze Images", 20, [
            ("Select visual features", 5),
            ("Detect objects and generate tags", 5),
            ("Extract text from images", 5),
            ("Convert handwritten text", 5),
        ]),
        ("Implement Custom Computer Vision Models", 25, [
            ("Train custom image models", 10),
            ("Evaluate custom vision model metrics", 5),
            ("Publish and consume custom vision models", 5),
        ]),
        ("Analyze Videos", 10, [
            ("Use AI Video Indexer", 5),
            ("Use AI Vision Spatial Analysis", 5),
        ]),
    ],
    "Implement NLP Solutions": [
        ("Analyze Text using Azure AI Language", 20, [
            ("Extract key phrases", 5),
            ("Extract entities", 5),
            ("Determine sentiment", 5),
            ("Detect language and PII", 5),
        ]),
        ("Process Speech using Azure AI Speech", 25, [
            ("Implement text-to-speech", 5),
            ("Implement speech-to-text", 5),
            ("Implement custom speech solutions", 5),
            ("Implement intent recognition", 5),
        ]),
        ("Translate Language", 20, [
            ("Translate text and documents", 5),
            ("Translate speech-to-speech", 5),
            ("Implement custom translation models", 5),
            ("Translate to multiple languages", 5),
        ]),
        ("Create a custom question answering solution", 15, [
            ("Create intents and add utterances", 5),
            ("Create entities", 5),
            ("Train and test a knowledge base", 5),
        ]),
    ],
    "Implement Knowledge Mining and Document Intelligence": [
        ("Implement an Azure AI Search Solution", 15, [
            ("Provision Azure AI Search resource", 5),
            ("Create data sources and indexes", 5),
            ("Run indexers", 5),
        ]),
        ("Implement an Azure AI Document Intelligence Solution", 15, [
            ("Provision a Document Intelligence resource", 5),
            ("Use prebuilt models to extract data", 5),
            ("Train and test custom document intelligence models", 5),
        ]),
    ],
    "Implement Generative AI Solutions": [
        ("Use Azure OpenAI Service to Generate Content", 20, [
            ("Provision Azure OpenAI resource", 5),
            ("Generate natural language and code", 5),
            ("Use DALL-E for image generation", 5),
            ("Use OpenAI APIs", 5),
        ]),
        ("Optimize Generative AI", 10, [
            ("Configure generative behavior", 5),
            ("Apply prompt engineering techniques", 5),
        ]),
    ],
}
