"""
Medical Knowledge Base - Semantic Search for Medical Information
"""

import os
import json

class MedicalKnowledgeBase:
    """
    Simple keyword-based knowledge base
    For production, use sentence-transformers + FAISS for semantic search
    """
    
    def __init__(self):
        self.documents = []
        self.data_dir = 'data'
    
    def load_knowledge(self):
        """Load medical knowledge from JSON"""
        knowledge_path = os.path.join(self.data_dir, 'medical_knowledge.json')
        
        if os.path.exists(knowledge_path):
            with open(knowledge_path, 'r') as f:
                self.documents = json.load(f)
            print(f"✅ Loaded {len(self.documents)} knowledge documents")
        else:
            print("⚠️ No knowledge base found")
            self.documents = []
    
    def search(self, query, top_k=3):
        """
        Simple keyword-based search
        Returns most relevant documents
        """
        query_lower = query.lower()
        query_words = set(query_lower.split())
        
        # Score each document
        scored_docs = []
        for doc in self.documents:
            content_lower = doc.get('content', '').lower()
            title_lower = doc.get('topic', '').lower()
            
            # Simple word matching score
            content_words = set(content_lower.split())
            title_words = set(title_lower.split())
            
            content_score = len(query_words & content_words)
            title_score = len(query_words & title_words) * 2  # Title matches worth more
            
            total_score = content_score + title_score
            
            if total_score > 0:
                scored_docs.append((doc, total_score))
        
        # Sort by score
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        
        # Return top_k results
        results = [doc for doc, score in scored_docs[:top_k]]
        
        if not results:
            # Return generic response
            return [{
                'topic': 'General Medical Advice',
                'content': 'Please consult with a healthcare professional for personalized medical advice.',
                'category': 'general'
            }]
        
        return results
    
    def get_by_category(self, category):
        """Get all documents in a category"""
        return [doc for doc in self.documents if doc.get('category') == category]
