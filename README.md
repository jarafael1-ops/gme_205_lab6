<<<<<<< HEAD
----create Table----
#Create table for Building
#Building-  









=======
# gme_205_lab6
>>>>>>> 81e97c2c2e42a6554a63f39ca1c6548fffac32b9



Part B Summary
- Briefly explain how the Lecture 6 case study was translated into Python.---I learned about the Lecture 6case srudy was how to translated into Pythin by converting the UML class diagram into an object-oriented system of classes, attributes, methods, inheritance and relationship. 

Guide questions:
1. What are the classes in your model? The SpatialObject class became the parent (base) class. It was designed to store shared spatial attributes such as geometry and common behavior that apply to  all spatial entties.
2.Which attributes became object state? The classes wa Parcel,Building and Road this was inherited from SpatialObject beacuse they all represnt spatial features. But the Household class did not inherit because from because it is a non-spatial object.
3.Which methods became behaviors?  The shared method implemented in the SpatialObject class was the distance_to(other) and intersects(other).
These methods were inherited by the Parcel, Building and Road to avoid the duplication and promoting code reuse.
4.Which relationships were hardest to implement? The following object relationships were implemented using object references: first A building is located on a Parcle, Second A Household lives in a Building and Lastly A Road is adjacent to ine or more Parcel objects.
These relationship were implemented by storing references or list objects inside the coreesponding classes making the system interconnected rather than isolated.

REFLECTION
1. What was easier to translate into code: attributes, methods, or inheritance? For me the easiest to translate into code was the attribute, base on my process in Python, the attributes aredirectly implemented as instance variables inside the init method, so they closely match what is shown in my UML Diagram. Each attribute in the UML simply became a variable assigned to self. The methods was slightly more complex because they required defining the logic or behavoir of the class, not just copying from the diagram. Inheritance was also more challenging than attributes because it was required understanding how the classes related to each other and how to properly parent and child classes. 
2. Which relationship in your UML was hardest to implement? For me the hardest implement was the inheritance because it was required managing how objects interact with each other rather than just defining them individually. For example, implementing this relationship involved passing objects as parameters, storing them in lists, or ensuring that one class correctly references another.Particulary maintaining proper communication between classes while avoiding tight coupling required careful design. This made the implementation more complex compared to simple attributes or methods.
3. Did your code exactly match your UML, or did you revise some parts during 
implementation?  My code did not exactly match the UML diagram,  I had to revise some parts during implementation. While my UML provide a clearprint, certain adjustments were necessary to make the code more practical and functional in Python.
For example, some methods needed additional parameters, and some relationships had to be simplified or restructured for easier implementation. These changes helped improve the clarity and efficiency of the code.
This shows that UML is a guide, but real implementation often requires flexibility and refinement.
4. What did you learn about the importance of OOAD from this exercise?For this exercise I learned the OOAD was so organizing and how to planning code before implementation. For me its so very helpful for the complex system into manageable classes, attributes and relationship.OOAD also makes easier to visualize how different parts of the system interact, its also reduces errors during coding. Overall learned for this exercise showed that a designed UML diagram can significantly simplfy the coding process evem though some adjustment may still be needed during the implementation. 

As you review or build this file, ask yourself: 
1.Why does SpatialObject own geometry? For this exercise the Spatialobjects we onws geomentry because it represents the most general concept of any object that exist in space. While OOP the parent class sjould contain all common attributes and behaviors shared by its subclasses.For example the Spatialobjects class onws geometry because all spatial entities require position or shape information. It also centralized the parent class consistency and reduces redundancy, allowing subclasses to focus only on their specialized features.
2.Why should distance_to() not be rewritten in every subclass? For this exercise the distance_to () should not be written because the logic for computing distance was generally the same for example usinf coordinates and formula like Euclidean distance. For the distance_to() method was implemented in the parent class to avoid duplication across subclasses. Since the formula for distance calculation is consisten, defining it once promotes reuse and ensure that all spatial objects behave uniformly.
3.How does this support abstraction and reuse?This design strongly supports both abstraction and reuse. 
Abstraction
1. SpatialObject hides the complexity of geometry handling.
2. Users of the class don’t need to know how distance is calculated internally.
3. Subclasses only interact with the interface (e.g., calling distance_to()).
Reuse
1. Shared attributes (geometry) and methods (distance_to()) are reused by all subclasses.
2. Developers don’t need to rewrite common logic.
3. akes the code easier to maintain and extend.
For example This design supports abstraction by hiding geometric computations within the SpatialObject class, allowing subclasses to use these features without understanding their internal implementation. It also promotes reuse by enabling all subclasses to inherit common attributes and methods, reducing redundancy and improving maintainability.

