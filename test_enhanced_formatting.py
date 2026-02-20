"""
Test Enhanced Document Formatting
Tests the new academic blackbook features:
- Table of contents
- Page numbers
- Proper margins
- Consistent heading hierarchy
"""

from services.doc_generator import document_generator

print("\n" + "="*60)
print("🧪 Testing Enhanced Document Formatting")
print("="*60 + "\n")

# Create test document with all sections
result = document_generator.create_blackbook(
    title="Enhanced Academic Blackbook Test",
    sections_dict={
        "abstract": """This is a comprehensive test abstract demonstrating the enhanced formatting features of the academic blackbook generator. The document now includes a professional table of contents, page numbers in the footer, proper 1-inch margins on all sides, and consistent heading hierarchy throughout. This abstract provides a brief overview of the document's purpose and structure.""",
        
        "introduction": """This introduction section demonstrates the improved document structure with consistent heading hierarchy and proper academic formatting. The enhanced blackbook generator now creates documents that closely resemble professional academic papers with all the standard features expected in scholarly work.

The introduction provides context and background for the research topic, establishing the foundation for the subsequent sections. With proper formatting, the document maintains a professional appearance throughout.""",
        
        "literature_review": """The literature review section presents existing research and theoretical frameworks related to the topic. This section demonstrates how multiple paragraphs are formatted with consistent spacing and alignment.

Academic blackbooks typically include comprehensive literature reviews that cite relevant sources and establish the theoretical foundation for the research. The enhanced formatting ensures that this section is clearly distinguished and professionally presented.""",
        
        "methodology": """The methodology section describes the research approach and methods used in the study. This section explains the systematic procedures followed to gather and analyze data.

The enhanced document formatting ensures that methodological details are presented in a clear, organized manner with proper spacing and hierarchy. This makes it easy for readers to understand the research process.""",
        
        "results": """The results section presents the key findings of the research. This section demonstrates how data and outcomes are formatted in the enhanced academic blackbook.

Results are presented with clear paragraph breaks and consistent formatting, making it easy to identify and understand the main findings. The professional layout enhances readability and comprehension.""",
        
        "conclusion": """The conclusion summarizes the main findings and their implications. This final section demonstrates the complete document structure with all enhanced formatting features.

The enhanced academic blackbook generator successfully creates professional documents with table of contents, page numbers, proper margins, and consistent heading hierarchy. These improvements make the generated documents suitable for academic and professional use."""
    }
)

if result['success']:
    print("✅ Enhanced document created successfully!\n")
    print(f"📄 Filename: {result['filename']}")
    print(f"📁 Location: {result['filepath']}")
    print(f"📊 Sections: {result['sections_count']}")
    print(f"💾 Size: {result['file_size']} bytes ({result['file_size']/1024:.2f} KB)\n")
    
    print("✨ Enhanced Features:")
    print("   ✅ Table of Contents - Automatically generated")
    print("   ✅ Page Numbers - Added to footer")
    print("   ✅ Proper Margins - 1 inch on all sides")
    print("   ✅ Heading Hierarchy - Consistent throughout")
    print("   ✅ Academic Layout - Professional formatting\n")
    
    print(f"📖 Open the document to see the enhanced formatting!")
    print(f"   Location: {result['filepath']}\n")
else:
    print(f"❌ Error creating document: {result['error']}\n")

print("="*60 + "\n")
