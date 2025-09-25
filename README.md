"# Unit-convertor--app-python" 
https://bmi-calculator-rameshajaved.streamlit.app/
# Streamlit ModuleNotFoundError Problem ka Solution (Roman Urdu)

## **Problem:**
Jab maine apna Streamlit project run kiya to mujhe yeh error mila:
```
ModuleNotFoundError: This app has encountered an error.
File "/mount/src/unit-convertor--app-python/app.py", line 3, in <module>
    from streamlit_lottie import st_lottie
```
Iska matlab tha ke **`streamlit-lottie`** module install nahi hai ya project ke andar properly available nahi hai.

---

## **Solution Steps:**

### **1. Streamlit-Lottie Install Karna**
Pehle maine yeh command run ki taake yeh module install ho jaye:
```
pip install streamlit-lottie
```

Agar koi aur module bhi missing ho, to usko bhi manually install karna hoga.

### **2. Virtual Environment Check Karna**
Agar virtual environment use kar rahe ho to ensure karo ke module **usi environment me install** ho.
Virtual environment activate karne ke baad install karo:
```
pip install streamlit-lottie
```

### **3. Correct Import Check Karna**
Kabhi kabhi module ka naam different hota hai. Isliye maine yeh bhi check kiya:
```python
import streamlit_lottie
```
Agar yeh error deta hai to iska matlab module properly install nahi hua.

### **4. Project Restart Karna**
Installation ke baad maine apna project dobara run kiya:
```
streamlit run app.py
```
Yeh step zaroori hai taake naye installed dependencies load ho sakein.

---

## **GitHub Par Project Update Karna**

### **1. `requirements.txt` File Generate Karna**
Jab ek naya module install hota hai, to use **GitHub par bhi update** karna hota hai. Iske liye maine yeh command run ki:
```
pip freeze > requirements.txt
```
Is command ne **`requirements.txt`** file update kar di jo saari dependencies list karti hai, including `streamlit-lottie`.

Agar manually add karna ho to file open karke likho:
```
streamlit-lottie==0.0.5
```

### **2. GitHub Par Changes Push Karna**
Ab maine apni **`requirements.txt`** file aur project changes GitHub par update kar diye:
```
git status
```
```
git add requirements.txt
```
```
git commit -m "Added streamlit-lottie dependency"
```
```
git push origin main
```
(Agar tumhara branch `main` nahi hai to `git branch` command se branch ka naam check kar lo aur `main` ki jagah uska naam likho.)

---

## **Deployment Issues Aur Solutions**

### **Agar Streamlit Cloud Ya GitHub Actions Par Deploy Kar Rahe Ho**
1. **Deployment Restart Karo**
   - Agar tum **Streamlit Cloud** use kar rahe ho to **Manage App** me jakar app **restart** kar do.
   - Agar tum **GitHub Actions** ya **Docker** use kar rahe ho to naye push ke baad automatic deploy ho jayega.

2. **Manually Dependencies Install Karni Ho To**
   - Agar koi aur user ya tum khud naye system par run kar rahe ho, to yeh command chalani hogi:
     ```
     pip install -r requirements.txt
     ```

---

## **Final Summary**
✔ Pehle **ModuleNotFoundError** aaya.
✔ `streamlit-lottie` install kiya.
✔ `requirements.txt` update kiya.
✔ GitHub par **push** kiya.
✔ Deployment restart ki aur successfully **project run ho gaya!** 🎉

Yeh notes future me help karenge agar koi aur dependency issue aaye. 🚀


