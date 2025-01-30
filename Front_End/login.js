function handleLogin(event) {
    event.preventDefault(); // منع الإرسال التقليدي للنموذج
    // هنا يتم التحقق من البيانات المدخلة
    // إذا كانت البيانات صحيحة، سيتم توجيه المستخدم إلى pro.html
    window.location.href = "pro.html"; // تأكد من صحة المسار
  }
  