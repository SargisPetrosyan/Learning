from abc import ABC, abstractmethod
from random import randrange
from typing import List

# ==========================================================
#  OBSERVER DESIGN PATTERN IMPLEMENTATION
# ==========================================================
# The Observer pattern defines a one-to-many dependency between objects so that 
# when one object (the Subject) changes its state, all its dependents (Observers)
# are automatically notified and updated.
#
# This is commonly used in event-driven systems, GUIs, and MVC architectures.
# ==========================================================


class Observer(ABC):
    """
    The Observer interface declares the `update` method, used by subjects
    to notify observers of any state changes.

    Each concrete observer implements this method to react appropriately
    when the subject changes state.
    """

    @abstractmethod
    def update(self, subject: "Subject") -> None:
        """
        Receive update from subject.

        Args:
            subject (Subject): The subject instance that triggered the update.
        """
        ...


class Subject(ABC):
    """
    The Subject interface declares methods for attaching, detaching, 
    and notifying observers.

    Concrete subjects maintain a list of observers and notify them 
    automatically whenever their internal state changes.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about a state change.
        """
        ...


class ConcreteSubject(Subject):
    """
    The ConcreteSubject contains important business logic that triggers 
    notifications whenever its internal state changes.

    Observers can query the subject for the latest state once notified.
    """

    def __init__(self) -> None:
        # The subject’s internal state that observers care about.
        self._state: int | None = None
        # List of observers subscribed to this subject.
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self) -> int | None:
        """
        Return the current state of the subject.
        """
        return self._state

    def some_business_logic(self) -> None:
        """
        Simulate business logic that changes the subject’s state.

        This method randomly changes the internal state and automatically 
        triggers notifications to all attached observers.
        """
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class ConcreteObserverA(Observer):
    """
    Concrete Observers react to the updates issued by the subject.

    In this example, ConcreteObserverA only reacts when the subject’s
    state is 0 or greater than or equal to 2.
    """

    def update(self, subject: Subject) -> None:
        # We use 'type: ignore' because the base Subject type does not
        # define `.state`, but ConcreteSubject does at runtime.
        if subject.state == 0 or subject.state >= 2:  # type: ignore
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    """
    Another concrete observer that reacts differently based on the
    subject's state.

    This class demonstrates how different observers can handle the same
    notification in unique ways.
    """

    def update(self, subject: Subject) -> None:
        if subject.state == 0 or subject.state >= 2:  # type: ignore
            print("ConcreteObserverB: Reacted to the event")


# ==========================================================
#  CLIENT CODE
# ==========================================================
# The client code creates subjects and observers, attaches observers
# to the subject, and triggers state changes.
# ==========================================================
if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)
    subject.some_business_logic()
