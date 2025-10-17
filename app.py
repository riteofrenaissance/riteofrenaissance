from flask import Flask, render_template, request, jsonify, session
import os
from datetime import datetime
from cores.claude_core import ClaudeCore
from routers.sovereign_router import SovereignRouter
from unifiers.response_unifier import ResponseUnifier

app = Flask(__name__)
app.secret_key = 'sovereign_ai_system_secret_2025'

# تهيئة المكونات الأساسية
claude_core = ClaudeCore()
sovereign_router = SovereignRouter()
response_unifier = ResponseUnifier()

@app.route('/')
def index():
    """الصفحة الرئيسية للنظام"""
    return render_template('index.html')

@app.route('/chat')
def chat():
    """واجهة الدردشة المتقدمة"""
    return render_template('chat.html')

@app.route('/dashboard')
def dashboard():
    """لوحة تحكم النظام"""
    return render_template('dashboard.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """API للدردشة مع نظام الذكاء الاصطناعي"""
    try:
        user_message = request.json.get('message', '')
        user_id = session.get('user_id', 'anonymous')
        
        if not user_message:
            return jsonify({'error': 'الرسالة فارغة'}), 400
        
        # تسجيل وقت البدء
        start_time = datetime.now()
        
        # توجيه الرسالة عبر نظام Sovereign المتكامل
        ai_response = sovereign_router.process_message(
            message=user_message,
            user_id=user_id,
            timestamp=start_time
        )
        
        # توحيد الاستجابة
        unified_response = response_unifier.unify(ai_response)
        
        # حساب وقت المعالجة
        processing_time = (datetime.now() - start_time).total_seconds()
        
        return jsonify({
            'success': True,
            'response': unified_response,
            'processing_time': f"{processing_time:.2f} ثانية",
            'user_id': user_id,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'خطأ في المعالجة: {str(e)}'
        }), 500

@app.route('/api/system/status')
def system_status():
    """حالة النظام والأنوية النشطة"""
    return jsonify({
        'status': 'active',
        'system': 'Sovereign AI System',
        'version': '1.0.0',
        'active_cores': ['claude', 'deepseek', 'gemini', 'chatgpt'],
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
